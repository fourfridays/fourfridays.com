from __future__ import absolute_import, unicode_literals

from django.db import models
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel

from wagtail.contrib.table_block.blocks import TableBlock

from wagtail.core.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, BooleanBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


from modelcluster.fields import ParentalKey


class AlignmentChoiceBlock(ChoiceBlock):
    choices = [
        ('normal', 'Normal'),
        ('text-left', 'Left'),
        ('text-center', 'Center'),
        ('text-right', 'Right'),
        ('text-justify', 'Justify'),
        ('text-nowrap', 'No Wrap')
    ]

class ImageAlignmentChoiceBlock(ChoiceBlock):
    choices = [
        ('left', 'Left'),
        ('right', 'Right'),
        ('center', 'Center'),
    ]

class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    image_alignment = ImageAlignmentChoiceBlock(required=False, default='left')

class AlignedRAWHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = AlignmentChoiceBlock(default='normal')


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('white-smoke', 'White Smoke'),
        ('aqua-island', 'Aqua Island'),
        ('concrete', 'Concrete')
    ))


class FontAwesomeIconSizeBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('lg', 'fa-lg'), 
        ('2x', 'fa-2x'),
        ('3x', 'fa-3x'),
        ('4x', 'fa-4x'),
        ('5x', 'fa-5x'),
    ))


class FontAwesomeIconTypeBlock(ChoiceBlock):
    choices = [
        ('solid', 'Solid'),
        ('regular', 'Regular'),
        ('light', 'Light'),
        ('brand', 'Brand')
    ]


class MaterialIconSizeBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('18', '18'), 
        ('24', '24'),
        ('36', '36'),
        ('48', '48'),
        ('60', '60'),
        ('72', '72'),
        ('84', '84'),
        ('96', '96'),
        ('108', '108'),
        ('120', '120'),
    ))


class PullQuoteBlock(StructBlock):
    quote = TextBlock('quote title')
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'


class IconBlock(StructBlock):
    font_awesome_icon_name = CharBlock(required=False)
    font_awesome_icon_size = FontAwesomeIconSizeBlock()
    font_awesome_icon_choice = FontAwesomeIconTypeBlock(required=False, default='solid')
    material_icon_name = CharBlock(required=False)
    material_icon_size = MaterialIconSizeBlock()
    alignment = AlignmentChoiceBlock(default='normal')

    class Meta:
        label = 'Icon'


class HtmlFormatBlock(StreamBlock):
    h1 = CharBlock(classname='title', help_text='Always use only one H1 per page')
    h2 = CharBlock(classname='title')
    h3 = CharBlock(classname='title')
    h4 = CharBlock(classname='title')
    h5 = CharBlock(classname='title')
    h6 = CharBlock(classname='title')
    paragraph = RichTextBlock()
    table = TableBlock(template='includes/table.html')
    image = ImageBlock()
    document = DocumentChooserBlock(icon='doc-full-inverse')
    embedded_video = EmbedBlock()
    lead_body = CharBlock(classname='lead')
    small_text = CharBlock(classname='small')
    blockquote = CharBlock(classname='blockquote')
    pull_quote = PullQuoteBlock()
    icon = IconBlock()
    raw_html = AlignedRAWHTMLBlock()


class SingleColumnBlock(StructBlock):
    column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'single_column_block.html'
        label = 'Single Column'


class TwoColumnBlock(StructBlock):
    left_column = HtmlFormatBlock()
    right_column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'two_column_block.html'
        label = 'Two Columns'


class ThreeColumnBlock(StructBlock):
    left_column = HtmlFormatBlock()
    middle_column = HtmlFormatBlock()
    right_column = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'three_column_block.html'
        label = 'Three Columns'


class FourColumnBlock(StructBlock):
    left_column_1 = HtmlFormatBlock()
    left_column_2 = HtmlFormatBlock()
    right_column_1 = HtmlFormatBlock()
    right_column_2 = HtmlFormatBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        template = 'four_column_block.html'
        label = 'Four Columns'


class HeroImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    alternate_text = CharBlock(help_text='Text for screen readers')
    caption = CharBlock(required=False, max_length=120, help_text='Caption will be shown below the image')
    fine_print = CharBlock(required=False, max_length=120, help_text='Fine Print will be shown below caption')
    overlay_text = BooleanBlock(required=False, help_text='If checked, caption is overlayed on image')
    photo_credit = CharBlock(required=False, max_length=80, help_text='This will show bottom right on the image')

    class Meta:
        template = 'hero_image_block.html'


class Pages(Page):
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),        
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('hero_image', HeroImageBlock(icon='image')),
    ],default='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]