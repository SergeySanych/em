# Generated by Django 4.2.9 on 2024-04-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_masterclasspage_mc_formtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclasspage',
            name='mc_formheader',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
