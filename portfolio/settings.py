from pathlib import Path

# database library import
import dj_database_url

# environ imports for creation of environment variables into .env file on root folder.
import environ
import os

# Cloudinary imports
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create environment variables into .env file on root folder
env = environ.Env()

# read environment variables from .env file
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Reference to SECRET_KEY environment variable from .env file.
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# print(f"ENVIRONMENT: {ENVIRONMENT}")
# print(f"DEBUG: {DEBUG}")

# DEVELOPMENT host:
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# PRODUCTION host:
else:
    ALLOWED_HOSTS = ['portfolio-app-t0qn.onrender.com', 'www.portfolio-app-t0qn.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    

    'feeds.apps.FeedsConfig',
    'ckeditor',
    'corsheaders',
    
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'temp')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# gunicorn will be the intermediate server between django and render
WSGI_APPLICATION = 'portfolio.wsgi.application'


# Deploying to render.com with postgres database:
# make use of dj-database-url package to bring in our External Database URL from render.com
# DATABASES = {
#     'default': dj_database_url.parse(env('DATABASE_URL'))
# }


# if not DEBUG means DEBUG = False
if not DEBUG:
    DATABASES = {
    "default": dj_database_url.parse(env("DATABASE_URL"))
}
    
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
   
    
    
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
    
if DEBUG:
    # Development settings
    # Use the default Django file storage for media files
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    
    # Static files configuration
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Media files configuration for user uploaded files:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    # Production settings
    # Configure Cloudinary using environment variables
    CLOUDINARY_URL = env('CLOUDINARY_URL').split('@')
    cloudinary.config(
        cloud_name=CLOUDINARY_URL[0].split(':')[0],
        api_key=CLOUDINARY_URL[0].split(':')[1],
        api_secret=CLOUDINARY_URL[1]
    )

    # Set Cloudinary as the default file storage for media files
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    
    # print(cloudinary.config().cloud_name)
    # print(cloudinary.config().api_key)
    # print(cloudinary.config().api_secret)
    


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS and CSRF configuration
CORS_ALLOW_ALL_ORIGINS = True
CSRF_COOKIE_SECURE = False # 

# Other deployment checks:

# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_COOKIE_NAME = 'sessionid'
# SESSION_SAVE_EVERY_REQUEST = False
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
# SESSION_COOKIE_PATH = '/'
# SESSION_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SECURE = False # 
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_COOKIE_AGE = 1209600
# SESSION_COOKIE_DOMAIN = None
# SESSION_CACHE_ALIAS = 'default'


# # Users can access the app over both HTTP and HTTPS.
# SECURE_HSTS_SECONDS = 0
# SECURE_SSL_REDIRECT = False #
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True


# Email settings
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = '---'
# EMAIL_HOST_PASSWORD = '---'
# EMAIL_USE_TLS = True