web: daphne mywebsite.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels_layer --settings=mywebsite.settings -v2