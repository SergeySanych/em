# Generated by Django 4.2.9 on 2024-04-05 10:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_reviewspage_review_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewspage',
            name='review_body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='subtitle')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('htmlcode', wagtail.blocks.RawHTMLBlock()), ('leftheader2', wagtail.blocks.StructBlock([('left', wagtail.blocks.CharBlock(required=False)), ('header_level', wagtail.blocks.IntegerBlock(default=3, help_text='Уровень заголовка', max_value=4, min_value=1)), ('color', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - blue, 2 - red')), ('position', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - external, 2 - internal')), ('right', wagtail.blocks.RichTextBlock(required=False)), ('rightcolor', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - blue, 2 - red')), ('rightborder', wagtail.blocks.RichTextBlock(required=False)), ('rightfinish', wagtail.blocks.RichTextBlock(required=False)), ('cta', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.CharBlock(required=False))])), ('reviewleftheader', wagtail.blocks.StructBlock([('left', wagtail.blocks.CharBlock(required=False)), ('header_level', wagtail.blocks.IntegerBlock(default=3, help_text='Уровень заголовка', max_value=4, min_value=1)), ('color', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - blue, 2 - red')), ('position', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - external, 2 - internal')), ('right', wagtail.blocks.RichTextBlock(required=False)), ('rightcolor', wagtail.blocks.IntegerBlock(default=0, help_text='0 - no, 1 - blue, 2 - red')), ('rightborder', wagtail.blocks.RichTextBlock(required=False)), ('rightfinish', wagtail.blocks.RichTextBlock(required=False)), ('cta', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.CharBlock(required=False))])), ('checklist2', wagtail.blocks.StructBlock([('bgimage', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.blocks.CharBlock()), ('beforechecklisttext', wagtail.blocks.TextBlock(required=False)), ('afterchecklisttext', wagtail.blocks.TextBlock(required=False)), ('checklist', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('inchecklist', wagtail.blocks.StructBlock([('listheader', wagtail.blocks.RichTextBlock(required=False)), ('checklist', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('checktext', wagtail.blocks.RichTextBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False))])))]))])))]))], blank=True, use_json_field=True),
        ),
    ]
