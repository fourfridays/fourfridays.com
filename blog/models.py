from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django import forms

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, StreamFieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index
from wagtail.wagtailsearch.models import Query

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, BooleanBlock, ChoiceBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from wagtail.contrib.table_block.blocks import TableBlock

from taggit.models import TaggedItemBase, Tag

from modelcluster.tags import ClusterTaggableManager
from modelcluster.fields import ParentalKey

import datetime

# Global Streamfield definition

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class BlogStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    aligned_html = AlignedHTMLBlock(icon="code", label='Raw HTML')
    document = DocumentChooserBlock(icon="doc-full-inverse")

    search_fields = Page.search_fields + [
        index.SearchField('paragraph'),
    ]


#Blog Index Page

class BlogIndexPage(Page):
    @property
    def blogs(self):
        # Get list of blog pages that are descendants of this page
        blogs = BlogPage.objects.descendant_of(self).live()
        blogs = blogs.order_by(
            '-first_published_at'
        ).select_related('owner').prefetch_related(
            'tagged_items__tag',
            'categories',
            'categories__category',
        )
        return blogs


    def get_context(self, request, tag=None, category=None, author=None, *args,
                    **kwargs):
        context = super(BlogIndexPage, self).get_context(
            request, *args, **kwargs)
        blogs = self.blogs

        if tag is None:
            tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__slug=tag)
        if category is None:  # Not coming from category_view in views.py
            if request.GET.get('category'):
                category = get_object_or_404(
                    BlogCategory, slug=request.GET.get('category'))
        if category:
            if not request.GET.get('category'):
                category = get_object_or_404(BlogCategory, slug=category)
            blogs = blogs.filter(categories__category__name=category)
        if author:
            if isinstance(author, str) and not author.isdigit():
                blogs = blogs.filter(author__username=author)
            else:
                blogs = blogs.filter(author_id=author)

        # Pagination
        page = request.GET.get('page')
        page_size = 5
        if hasattr(settings, 'BLOG_PAGINATION_PER_PAGE'):
            page_size = settings.BLOG_PAGINATION_PER_PAGE

        if page_size is not None:
            paginator = Paginator(blogs, page_size)  # Show 10 blogs per page
            try:
                blogs = paginator.page(page)
            except PageNotAnInteger:
                blogs = paginator.page(1)
            except EmptyPage:
                blogs = paginator.page(paginator.num_pages)

        context['blogs'] = blogs
        context['category'] = category
        context['tag'] = tag
        context['author'] = author
        context = get_blog_context(context)

        return context

    class Meta:
        verbose_name = _('Blog index')
        #subpage_types = ['blog.BlogPage']


def get_blog_context(context):
    """ Get context data useful on all blog related pages """
    context['authors'] = get_user_model().objects.filter(
        owned_pages__live=True,
        owned_pages__content_type__model='blogpage'
    ).annotate(Count('owned_pages')).order_by('-owned_pages__count')
    context['all_categories'] = BlogCategory.objects.all()
    context['root_categories'] = BlogCategory.objects.filter(
        parent=None,
    ).prefetch_related(
        'children',
    ).annotate(
        blog_count=Count('blogpage'),
    )
    return context


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(
        max_length=80, unique=True, verbose_name=_('Category Name'))
    slug = models.SlugField(unique=True, max_length=80)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name="children",
        help_text=_(
            'Categories, unlike tags, can have a hierarchy. You might have a '
            'Jazz category, and under that have children categories for Bebop'
            ' and Big Band. Totally optional.')
    )
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    panels = [
        FieldPanel('name'),
        FieldPanel('parent'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError('Parent category cannot be self.')
            if parent.parent and parent.parent == self:
                raise ValidationError('Cannot have circular Parents.')

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            count = BlogCategory.objects.filter(slug=slug).count()
            if count > 0:
                slug = '{}-{}'.format(slug, count)
            self.slug = slug
        return super(BlogCategory, self).save(*args, **kwargs)


class BlogCategoryBlogPage(models.Model):
    category = models.ForeignKey(
        BlogCategory, related_name="+", verbose_name=_('Category'))
    page = ParentalKey('BlogPage', related_name='categories')
    panels = [
        FieldPanel('category'),
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


@register_snippet
class BlogTag(Tag):
    class Meta:
        proxy = True


def limit_author_choices():
    """ Limit choices in blog author field based on config settings """
    LIMIT_AUTHOR_CHOICES = getattr(settings, 'BLOG_LIMIT_AUTHOR_CHOICES_GROUP', 'Editors')
    if LIMIT_AUTHOR_CHOICES:
        if isinstance(LIMIT_AUTHOR_CHOICES, str):
            limit = Q(groups__name=LIMIT_AUTHOR_CHOICES)
        else:
            limit = Q()
            for s in LIMIT_AUTHOR_CHOICES:
                limit = limit | Q(groups__name=s)
        if getattr(settings, 'BLOG_LIMIT_AUTHOR_CHOICES_ADMIN', False):
            limit = limit | Q(is_staff=True)
    else:
        limit = {'is_staff': True}
    return limit


#Blog Page
class BlogPage(Page):
    date = models.DateField(
        _("Post date"), default=datetime.datetime.today,
        help_text=_("This date may be displayed on the blog post. It is not "
                    "used to schedule posts to go live at a later date.")
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True,
        limit_choices_to=limit_author_choices,
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        related_name='author_pages',
    )


    body = StreamField(BlogStreamBlock())

    blog_categories = models.ManyToManyField(
        BlogCategory, through=BlogCategoryBlogPage, blank=True)
    
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def save_revision(self, *args, **kwargs):
        if not self.author:
            self.author = self.owner
        return super(BlogPage, self).save_revision(*args, **kwargs)

    def get_absolute_url(self):
        return self.url

    def recent_posts(self):
        recent_posts = BlogPage.objects.live()
        recent_posts = recent_posts.order_by('-first_published_at')[:3] 
        return recent_posts

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context = get_blog_context(context)
        context['recent_posts'] = self.recent_posts()
        
        return context

    class Meta:
        verbose_name = _('Blog page')
        verbose_name_plural = _('Blog pages')

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('author'),
    StreamFieldPanel('body'),
    MultiFieldPanel([
        FieldPanel('tags'),
        InlinePanel('categories', label=_("Categories")),
    ]),
]
