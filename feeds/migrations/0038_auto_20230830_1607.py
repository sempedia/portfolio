# Generated by Django 3.2.16 on 2023-08-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0037_auto_20230830_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(null=True, upload_to='about'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(null=True, upload_to='contact'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='projects_images'),
        ),
    ]
