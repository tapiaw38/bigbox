#!/bin/bash


python /app/manage.py collectstatic --noinput

echo "$@"
exec "$@"