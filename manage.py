#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import environ
import os
import sys


# Create environment variables into .env file on root folder
env = environ.Env()

# read environment variables from .env file
environ.Env.read_env()
    
def main():
    """Run administrative tasks."""
    print(env('ENVIRONMENT'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.settings_dev' if env('ENVIRONMENT') == 'DEVELOPMENT' else 'portfolio.settings.settings_prod')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)