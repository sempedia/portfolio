# Generated by Django 3.2.16 on 2023-08-28 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0032_auto_20230829_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='images/about.png', null=True, upload_to='about'),
        ),
    ]
