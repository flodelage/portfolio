# Generated by Django 4.0.4 on 2022-05-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_bio_remove_profile_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
