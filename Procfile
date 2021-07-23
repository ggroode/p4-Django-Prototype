release: python manage.py migrate
web: gunicorn p4.wsgi
worker: python manage.py runworker channel_layer