release: python manage.py migrate
web: gunicorn website.wsgi:application --log-file -
python manage.py collectstatic --noinput
