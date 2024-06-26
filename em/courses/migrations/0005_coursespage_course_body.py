# Generated by Django 4.2.9 on 2024-03-19 14:52

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_coursespage_course_icon1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursespage',
            name='course_body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='subtitle')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('htmlcode', wagtail.blocks.RawHTMLBlock()), ('checklist', wagtail.blocks.StructBlock([('bgimage', wagtail.images.blocks.ImageChooserBlock()), ('checklist', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('checktext', wagtail.blocks.TextBlock(max_length=200, required=False)), ('text', wagtail.blocks.TextBlock(max_length=200, required=False))])))]))], blank=True, use_json_field=True),
        ),
    ]
