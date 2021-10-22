#!/bin/bash


python /app/manage.py collectstatic --noinput
python /app/manage.py makemigrations
python /app/manage.py migrate
python manage.py loaddata data.json

echo "$@"
exec "$@"