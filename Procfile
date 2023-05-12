web : daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem mywebsite.asgi:application
worker: python manage.py runworker channels_layer --settings=mywebsite.settings -v2