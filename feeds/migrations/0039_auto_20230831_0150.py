# Generated by Django 3.2.16 on 2023-08-30 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0038_auto_20230830_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='image',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='image',
        ),
    ]
