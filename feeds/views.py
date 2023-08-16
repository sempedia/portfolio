from django.shortcuts import render
from .models import PersonalInformation, About, Project, Skill

# Create your views here.


def home(request):
    personal_info = PersonalInformation.objects.all()
    about = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'personal_info': personal_info,
        'about': about,
        'projects': projects,
        'skills': skills
    }

    return render(request, 'home.html', context)
