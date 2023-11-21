#!/bin/sh
echo "start scripts"
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser --no-input
python manage.py createsuperuser_if_not_exist

exec "$@"