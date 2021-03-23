# Generated by Django 2.2.13 on 2021-03-09 13:52

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0015_auto_20210309_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenter',
            name='image_alt_1',
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='image_alt_height',
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='image_alt_width',
        ),
        migrations.AlterField(
            model_name='presenter',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='image_height', null=True, upload_to='presenters/', verbose_name='Image', width_field='image_width'),
        ),
    ]