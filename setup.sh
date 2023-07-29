#!/bin/bash

# inicializa el ambiente virtual
python3 -m venv .venv
source ./.venv/bin/activate
pip install django gunicorn psycopg

# realiza las migraciones
python manage.py migrate