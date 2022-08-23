release: python manage.py migrate
web: gunicorn blog.wsgi:application --log-file -
python manage.py collectstatic --noinput
