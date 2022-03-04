from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import ImageGridBlock, BaseStreamBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock


class StandardPage(Page):
    # Hero section of Page
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    hero_heading = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='40 character limit.'
        )
    hero_caption = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='140 character limit.'
        )
    hero_photo_credit = models.CharField(
        null=True,
        blank=True,
        max_length=80,
        help_text='80 character limit. This will show on the bottom right on the image'
        )
    hero_cta = models.CharField(
        null=True,
        blank=True,
        verbose_name='Hero CTA',
        max_length=20,
        help_text='Text to display on Call to Action. 20 character limit.'
        )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link the Call to Action'
    )
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ],default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_heading', classname='full'),
            FieldPanel('hero_caption', classname='full'),
            FieldPanel('hero_photo_credit', classname='full'),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                PageChooserPanel('hero_cta_link'),
                ])
            ], heading='Hero Image'),
        StreamFieldPanel('body'),
    ]