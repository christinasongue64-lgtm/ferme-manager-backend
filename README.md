# Ferme Manager - Backend

API REST Django pour la gestion d'élevage.

## Technologies
- Django 5.0
- Django REST Framework
- MySQL
- JWT Authentication

## Installation
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env# Ferme Manager - Backend

API REST Django pour la gestion d'élevage développée dans le cadre du projet de fin d'année à l'Institut Universitaire Saint Jean 2025-2026.

## Description
Ferme Manager Backend est une API RESTful qui fournit tous les services nécessaires à la gestion d'un élevage : authentification, gestion des animaux, suivi sanitaire, stocks, ventes et finances.

## Technologies
- Django 5.0
- Django REST Framework
- MySQL
- JWT Authentication
- WhiteNoise

## Installation
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints
- `/api/auth/login/` - Connexion
- `/api/auth/register/` - Inscription
- `/api/animals/` - Gestion des animaux
- `/api/health/` - Suivi sanitaire
- `/api/stock/` - Gestion du stock
- `/api/sales/` - Ventes
- `/api/finance/` - Finances
- `/api/dashboard/` - Tableau de bord

## Accès
- **API** : http://127.0.0.1:8000
- **Admin** : http://127.0.0.1:8000/admin
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints
- `/api/auth/login/` - Connexion
- `/api/animals/` - Gestion des animaux
- `/api/health/` - Suivi sanitaire
- `/api/stock/` - Gestion du stock
- `/api/sales/` - Ventes
- `/api/finance/` - Finances
- `/api/dashboard/` - Tableau de bord