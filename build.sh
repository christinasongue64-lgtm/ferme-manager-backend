#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
#!/bin/bash

# Mettre à jour et installer les dépendances système nécessaires
apt-get update
apt-get install -y default-libmysqlclient-dev gcc pkg-config

# Installer les dépendances Python
pip install -r requirements.txt