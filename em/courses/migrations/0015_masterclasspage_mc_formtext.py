# Generated by Django 4.2.9 on 2024-04-02 13:07

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_mcformfield_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclasspage',
            name='mc_formtext',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
