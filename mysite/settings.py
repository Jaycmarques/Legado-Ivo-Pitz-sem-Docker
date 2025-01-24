"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(BASE_DIR, 'dotenv_files', '.env')
load_dotenv(dotenv_path)



# DOTENV
load_dotenv(BASE_DIR.parent / 'dotenv_files' / '.env', override=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY="!l@5kahdte8w#tlg5+u4z_)vq9k1_h3r13+q$5d7qk7npz#6t2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', 0)))

ALLOWED_HOSTS = [
    h.strip() for h in os.getenv('ALLOWED_HOSTS', '127.0.0.1, localhost').split(',') if h.strip()
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'axes',
    'pages',
    'familytree',
    'ordered_model',
]

MIDDLEWARE = [
    'axes.middleware.AxesMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'familytree', 'templates', 'familytree'),
        os.path.join(BASE_DIR, 'pages', 'templates', 'pages'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'pages.context_processors.listar_pages',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ], }, },]


WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'psql',  # Nome do serviço no docker-compose
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{
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
},]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# URL para acessar arquivos estáticos na aplicação
STATIC_URL = '/static/'

# Diretório onde os arquivos estáticos são coletados
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretórios adicionais para procurar arquivos estáticos
STATICFILES_DIRS = [
    # Adicione o caminho correto para arquivos estáticos de aplicativos
    os.path.join(BASE_DIR, 'pages', 'static'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AXES
AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

AXES_ENABLED = True
AXES_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = 1  # 1 Hora
AXES_RESET_ON_SUCCESS = True

INTERNAL_IPS = [
    "127.0.0.1",        # Loopback para acessos locais
    "192.168.10.22",    # IP da sua máquina na rede local
    "172.17.0.1",       # IP interno do Docker
    "172.18.0.1",       # IP interno do Docker
    "172.19.0.1",       # IP interno do Docker
]

