# Generated by Django 3.2.16 on 2023-08-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0021_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('skill', models.TextField(blank=True, max_length=230, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images'),
        ),
    ]
