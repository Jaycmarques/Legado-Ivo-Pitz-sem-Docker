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
import dj_database_url

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

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = bool(int(os.getenv('DEBUG', 0)))
DEBUG = True

# ALLOWED_HOSTS = [
#     h.strip() for h in os.getenv('ALLOWED_HOSTS', '127.0.0.1, localhost').split(',') if h.strip()
# ]
ALLOWED_HOSTS = ['legado-ivo-pitz-production-8c61.up.railway.app', 'www.legado-ivo-pitz-production-8c61.up.railway.app', 'localhost', '127.0.0.1']


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
    'django_summernote',
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
    'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Apenas um diretório global
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'pages.context_processors.listar_pages',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]


WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
    )
}
     
 # Usando a variável já configurada no Railway
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('POSTGRES_DB'),
#         'USER': os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST': 'psql',  # Nome do serviço no docker-compose
#         'PORT': '5432',
#     }
# }


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

LANGUAGE_CODE = 'pt-br'

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
    os.path.join(BASE_DIR, 'familytree', 'static'),
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


SUMMERNOTE_CONFIG = {
    'width': '100%',  # Ajuste da largura
    'height': 500,  # Altura do editor
    # Configuração geral do Summernote
    'summernote': {
        'toolbar': [
            ['insert', ],
        ],
        'lang': 'pt-BR',
    },

    # Configuração de restrições para upload
    'attachment_require_authentication': True,  # Exige autenticação para uploads
    'attachment_filesize_limit': 2 * 1024 * 1024,  # Limite de tamanho: 2MB
    'attachment_file_extensions': ['jpg', 'jpeg', 'png'],  # Apenas imagens JPG e PNG são permitidas

    # Configuração de Tooltips e Popovers
    'popover': {
        'image': [
            ['custom', '<small>Somente imagens JPG ou PNG. Clique no botão ao lado para upload!</small>']
        ],
    },

}



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

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 ano
# SECURE_HSTS_SECONDS = 0

# Desativa o suporte a HTTP em servidores não seguros
SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# # Forçar SSL (HTTPS)
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Cookies seguros
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True