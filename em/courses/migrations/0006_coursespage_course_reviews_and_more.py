# Generated by Django 4.2.9 on 2024-03-21 14:05

from django.db import migrations
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('courses', '0005_coursespage_course_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursespage',
            name='course_reviews',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='reviews.reviewspage'),
        ),
        migrations.AlterField(
            model_name='coursespage',
            name='course_body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='subtitle')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('htmlcode', wagtail.blocks.RawHTMLBlock()), ('leftheader', wagtail.blocks.StructBlock([('left', wagtail.blocks.CharBlock()), ('right', wagtail.blocks.RichTextBlock()), ('cta', wagtail.blocks.CharBlock(required=False))])), ('checklist', wagtail.blocks.StructBlock([('bgimage', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.blocks.CharBlock()), ('beforechecklisttext', wagtail.blocks.TextBlock(required=False)), ('afterchecklisttext', wagtail.blocks.TextBlock(required=False)), ('checklist', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('checktext', wagtail.blocks.TextBlock(max_length=250, required=False)), ('text', wagtail.blocks.TextBlock(max_length=250, required=False))])))]))], blank=True, use_json_field=True),
        ),
    ]
