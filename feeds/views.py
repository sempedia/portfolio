
from django.shortcuts import render
from django.conf import settings
from .models import PersonalInformation, About, Project, Skill
from .forms import ProjectForm
from .cloudinary_config import uploader  # Import the uploader from your Cloudinary configuration module
import messages

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
            # Upload the file to Cloudinary
            file_to_upload = form.cleaned_data['your_file_field_name']
            result = uploader.upload(file_to_upload)
            cloudinary_url = result['secure_url']  # Get the Cloudinary URL of the uploaded file
            # You can save the `cloudinary_url` or use it as needed
            # ...

        # ...
    context = {
        'personal_info': personal_info,
        'about': about,
        'projects': projects,
        'skills': skills,
        'project_form': project_form,  # Renamed the variable for consistency
        'is_development': is_development,
    }

    return render(request, 'feeds/home.html', context)
