#!/bin/bash

# evita el error de acceso denegado a la carpeta actual
cd /tmp

# ejecuta los comandos SQL
sudo -u postgres psql << EOF
CREATE USER django_user WITH PASSWORD 'django_pass';
CREATE DATABASE django_db;
EOF