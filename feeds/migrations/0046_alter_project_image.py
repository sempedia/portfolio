# Generated by Django 3.2.16 on 2023-09-03 23:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0045_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
