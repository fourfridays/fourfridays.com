# Generated by Django 2.2.5 on 2019-10-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20191005_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='hero_photo_credit',
            field=models.CharField(blank=True, help_text='80 character limit. This will show on the bottom right on the image', max_length=80, null=True),
        ),
    ]
