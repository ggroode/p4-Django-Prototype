release: python manage.py migrate
web: gunicorn p4.routing
worker: python manage.py runworker channel_layer