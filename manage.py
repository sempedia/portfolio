#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

# Create environment variables into .env file on root folder
env = environ.Env()

# Read environment variables from .env file
environ.Env.read_env()

def main():
    """Run administrative tasks."""
    # Determine the environment context (development, production, etc.)
    # You can set the ENVIRONMENT variable in your .env file.
    # For example, ENVIRONMENT=development or ENVIRONMENT=production
    ENVIRONMENT = env('ENVIRONMENT')

    # Set the appropriate DJANGO_SETTINGS_MODULE based on the environment
    if ENVIRONMENT == 'DEVELOPMENT':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    elif ENVIRONMENT == 'PRODUCTION':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
    else:
        raise ValueError("Invalid environment. Set ENVIRONMENT to DEVELOPMENT or PRODUCTION in your .env file.")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
