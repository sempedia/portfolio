# Generated by Django 3.2.16 on 2023-08-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0031_auto_20230829_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='images/about.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, default='images/contact_me.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='avatar',
            field=models.ImageField(default='images/home.png', null=True, upload_to=''),
        ),
    ]