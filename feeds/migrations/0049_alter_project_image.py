# Generated by Django 3.2.16 on 2023-09-21 23:59

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0048_auto_20230922_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='projects/'),
        ),
    ]
