release: python manage.py migrate
web: gunicornstorefront.wsgi
worker: celery -A storefront worker