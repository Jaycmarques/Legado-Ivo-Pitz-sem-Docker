web: python manage.py migrate && python manage.py createsuperuser --noinput || true && python manage.py collectstatic --noinput && gunicorn mysite.wsgi
