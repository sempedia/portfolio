# Generated by Django 3.2.16 on 2023-08-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0020_auto_20230815_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
