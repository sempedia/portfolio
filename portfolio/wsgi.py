"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Render deployment
application = get_wsgi_application()
application = WhiteNoise(application)


# HEROKU DEPLOYMENT
# application = get_wsgi_application()

# VERCEL DEPLOYMENT
# app = application

