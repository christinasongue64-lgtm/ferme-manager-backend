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
cp .env.example .env
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