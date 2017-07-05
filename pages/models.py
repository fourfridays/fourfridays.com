from __future__ import absolute_import, unicode_literals

from django.db import models
from django import forms

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.contrib.table_block.blocks import TableBlock

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

class PullQuoteBlock(StructBlock):
    quote = TextBlock('quote title')
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('white-smoke', 'White Smoke'),
        ('aqua-island', 'Aqua Island')
    ))


class SingleColumnBlock(StructBlock):
    column = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'single_column_block.html'
        icon = 'placeholder'
        label = 'Single Column'


class TwoColumnBlock(StructBlock):
    left_column = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    right_column = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class FourColumnBlock(StructBlock):
    left_column_1 = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    left_column_2 = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    right_column_1 = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    right_column_2 = StreamBlock([
        ('h2', CharBlock(classname='title')),
        ('h3', CharBlock(classname='title')),
        ('h4', CharBlock(classname='title')),
        ('paragraph', RichTextBlock()),
        ('table', TableBlock(template='includes/table.html')),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock(icon='doc-full-inverse')),
        ('embedded_video', EmbedBlock()),
        ('lead_body', CharBlock(classname='lead')),
        ('small_text', CharBlock(classname='small')),
        ('blockquote', CharBlock(classname='blockquote')),
        ('pull_quote', PullQuoteBlock()),
        ('raw_html', RawHTMLBlock()),
    ],label='Body')
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'four_column_block.html'
        label = 'Four Columns'


class Pages(Page):
    body = StreamField([
        ('single_column', SingleColumnBlock()),
        ('two_columns', TwoColumnBlock()),
        ('four_columns', FourColumnBlock()),
    ],default='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]