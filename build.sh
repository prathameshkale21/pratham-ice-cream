#!/usr/bin/env bash
# Render runs this automatically on every deploy.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py clear_catalog

python manage.py create_admin
