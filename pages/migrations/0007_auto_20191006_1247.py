# Generated by Django 2.2.5 on 2019-10-06 12:47

from django.db import migrations
import pages.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20191006_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.fields.StreamField([('single_column', wagtail.blocks.StructBlock([('column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('two_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('three_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('middle_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('four_columns', wagtail.blocks.StructBlock([('left_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('left_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Design')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('image_grid', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))], help_text='Minimum 2 blocks and a maximum of 4 blocks', icon='image', max_num=4, min_num=2))], default=''),
        ),
    ]
