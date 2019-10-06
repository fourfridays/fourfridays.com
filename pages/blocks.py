from django import forms

from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    BooleanBlock, CharBlock, ChoiceBlock, FieldBlock, PageChooserBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock
)


class AlignmentBlock(ChoiceBlock):
    choices = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right')
    ]


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('white-smoke', 'White Smoke'),
        ('aqua-island', 'Aqua Island'),
        ('concrete', 'Concrete')
    ))


class IconBlock(StructBlock):
    icon = ChoiceBlock([
        ('font-awesome', 'Font Awesome'),
        ('material-icon', 'Material Icon')
    ])
    name = CharBlock(max_length=25, help_text='25 character limit')
    size = ChoiceBlock(choices = [
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large'),
        ('xl', 'Extra Large')
    ])
    font_awesome_icon_choice = ChoiceBlock([
        ('solid', 'Solid'),
        ('regular', 'Regular'),
        ('light', 'Light'),
        ('brand', 'Brand')
    ], required=False)
    alignment = AlignmentBlock(default='left')

    class Meta:
        label = 'Icon'
        template = 'blocks/icon_block.html'


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alignment = AlignmentBlock(default='left', required=False)
    border = BooleanBlock(required=False, help_text='Adds border around image')

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'


class ImageGridBlock(StreamBlock):
    grid = StructBlock([
        ('image', ImageChooserBlock(required=True, help_text='size: 800X450px')),
        ('caption', CharBlock(max_length=26, help_text='26 characters limit')),
        ('description', CharBlock(max_length=300, required=False, help_text='300 characters limit')),
        ('link', PageChooserBlock(required=False))
    ])

    class Meta:
        template = 'blocks/image_grid_block.html'


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h6 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6')
    ], blank=True, required=False)
    alignment = AlignmentBlock(default='left', required=False)

    class Meta:
        icon = 'title'
        template = 'blocks/heading_block.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html'
    )
    image_block = ImageBlock()
    image_grid_block = ImageGridBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-s15',
        template='blocks/embed_block.html')
    icon_block = IconBlock()


class SingleColumnBlock(StructBlock):
    column = BaseStreamBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        label = 'Single Column'
        template = 'blocks/single_column_block.html'


class TwoColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        label = 'Two Columns'
        template = 'blocks/two_column_block.html'


class ThreeColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    middle_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        label = 'Three Columns'
        template = 'blocks/three_column_block.html'


class FourColumnBlock(StructBlock):
    left_column_1 = BaseStreamBlock()
    left_column_2 = BaseStreamBlock()
    right_column_1 = BaseStreamBlock()
    right_column_2 = BaseStreamBlock()
    background_color = BackgroundColorBlock()

    class Meta:
        label = 'Four Columns'
        template = 'blocks/four_column_block.html'