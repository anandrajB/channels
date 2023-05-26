web: gunicorn mywebsite.asgi:application -k uvicorn.workers.UvicornWorker
worker: python manage.py runworker channels_layer --settings=mywebsite.settings -v2

