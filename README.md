# django-channels-basic-chat

Tutorial link: https://youtu.be/cw8-KFVXpTE

2323
## Cloning and starting project
1. - git clone https://github.com/divanov11/django-channels-basic-chat
2. - cd django-channels-basic-chat
3. - pip install -r requirements.txt
4. - python manage.py runserver



gunicorn mywebsite.asgi:application -k uvicorn.workers.UvicornWorker