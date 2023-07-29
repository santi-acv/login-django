#!/bin/bash

# inicializa el ambiente virtual
python -m venv .venv
source ./.venv/bin/activate
pip install django gunicorn psycopg

# realiza las migraciones
python project/manage.py migrate