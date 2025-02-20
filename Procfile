web: python manage.py migrate && python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME && python manage.py collectstatic --noinput && gunicorn mysite.wsgi
