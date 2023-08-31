# Generated by Django 3.2.16 on 2023-08-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0035_alter_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/about'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, default='images/contact_me.svg', null=True, upload_to='media/contact'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='avatar',
            field=models.ImageField(default='images/home.png', null=True, upload_to='media/avatar'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/projects_images'),
        ),
    ]