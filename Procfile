web: python manage.py migrate && \
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME && \
python manage.py collectstatic --noinput && \
python manage.py populate_tree familytree/TreeFromWebsite.txt && \
gunicorn mysite.wsgi
