#!/bin/sh


python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:8000
# run with gunicorn
gunicorn project_stafl.wsgi:application --bind 0.0.0.0:8000
