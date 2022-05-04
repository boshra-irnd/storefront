# storefront
Storefront is a RESTful Store  to learn and practice Django and Django Rest Framework.


## Features
- Authentication with email using JWT
- Adding new Collection and Products to store by admin
- Viewing products by customers and add them to their cart
- Add new items to cart or update quantity of existing item
- Make an order by customers
- Automatically remove shopping cart after making order
- Ability to view and update user profiles for customers and admins
- Easy insatllation
- Production-ready configuration for Static Files, Database Settings, Gunicorn, Docker
- Cloud-native design using 12-factor methodology

## Technologies used
- [Python 3.9](https://www.python.org/) - Programming Language
- [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - For Building RESTful APIs
- [Pytest](https://docs.pytest.org/en/7.0.x/) - Automated Testing
- [Docker](https://www.docker.com/) - Container Platform
- [MySQL](https://www.mysql.com/) - Database
- [Git](https://git-scm.com/doc) - Version Control System
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
- [Celery](https://github.com/celery/celery) - Task Queue
- [Flower](https://github.com/mher/flower) - Monitoring Celery Tasks
- [Locust](https://github.com/locustio/locust) - Performance Testing
- [Silk](https://github.com/jazzband/django-silk) - Profiling

## docker-compose
run docker-compose up [-d]


## Setup
(local) pip install -r requirements.txt && python manager.py runserver

(pipenv) pipenv install && pipenv shell && pyton mnager.py runserver
