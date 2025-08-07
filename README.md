# Amoozeshgah Backend

A Django-based backend project with Celery and Celery Beat for background and periodic task processing.

## Features

- Built with Django and Django REST Framework
- Asynchronous task processing with Celery
- Periodic tasks using Celery Beat (e.g., checking receipts every 30 seconds)
- Redis as a message broker

## Requirements

- Python 3.8+
- Redis
- PostgreSQL or SQLite
- Django
- Celery

## Installation

```bash
git clone https://github.com/your-username/amoozeshgah_backend.git
cd amoozeshgah_backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
