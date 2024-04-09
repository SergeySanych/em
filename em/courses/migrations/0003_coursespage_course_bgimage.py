# Generated by Django 4.2.9 on 2024-03-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('courses', '0002_coursespage_course_icon1_coursespage_course_icon2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursespage',
            name='course_bgimage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
