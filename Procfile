release: python manage.py migrate && python manage.py createsuperuser --noinput || true
web: gunicorn config.wsgi --bind 0.0.0.0:$PORT --workers 2
