#!/bin/bash

set -e

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

echo "STARTING GUNICORN SERVER..."
gunicorn config.wsgi:application --bind :8000