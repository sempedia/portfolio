
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html
from PIL import Image


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(null=True, default='images/home.png')
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    cv = models.FileField(upload_to='cv', blank=True, null=True)
   
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name_complete

class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    image = models.ImageField(blank=True, null=True, default='images/about.png')
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, default='images/contact_me.svg')
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

    
class Skill(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.skill    

class Project(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.title

