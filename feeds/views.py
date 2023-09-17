from django.shortcuts import render
from .models import PersonalInformation, About, Project, Skill
from django import forms

from cloudinary.forms import cl_init_js_callbacks    
from .models import Project
from .forms import ProjectForm

# Create your views here.


def home(request):
    personal_info = PersonalInformation.objects.all()
    about = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    # for Cloudinary images upload
    backed_form = ProjectForm()
    context = {
        'personal_info': personal_info,
        'about': about,
        'projects': projects,
        'skills': skills,
        'backend_form': backed_form,
    }
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()


    return render(request, 'feeds/home.html', context)
