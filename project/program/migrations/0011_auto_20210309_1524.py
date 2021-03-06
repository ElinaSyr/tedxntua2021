# Generated by Django 2.2.13 on 2021-03-09 13:24

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0010_auto_20210309_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='image_alt',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='image_alt_height',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='image_alt_width',
        ),
        migrations.AddField(
            model_name='presenter',
            name='image_alt',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='image_alt_height', null=True, upload_to='presenters/', verbose_name='Image 2', width_field='image_alt_width'),
        ),
        migrations.AddField(
            model_name='presenter',
            name='image_alt_height',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='presenter',
            name='image_alt_width',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
