
from django.shortcuts import render
from django.conf import settings
from .models import PersonalInformation, About, Project, Skill
from .forms import ProjectForm
from django.contrib import messages

def home(request):
    # Query relevant data
    personal_info = PersonalInformation.objects.all()
    about = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    # Determine if in development mode
    is_development = settings.DEBUG
    
    # Initialize an empty form
    project_form = ProjectForm()
    
    # Handle POST request for form submission
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully.')  # Provide a success message
        else:
            messages.error(request, 'Error adding project. Please check your input.')  # Provide an error message if form is invalid
    
    context = {
        'personal_info': personal_info,
        'about': about,
        'projects': projects,
        'skills': skills,
        'project_form': project_form,  # Renamed the variable for consistency
        'is_development': is_development,
    }

    return render(request, 'feeds/home.html', context)
