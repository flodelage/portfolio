# Generated by Django 4.0.4 on 2022-05-23 16:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_project_repository_alter_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='work',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
