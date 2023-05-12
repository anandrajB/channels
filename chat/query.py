import json
from channels.generic.websocket import WebsocketConsumer ,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import name

from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async 
from .ser import PartyaccountsSerializer
from django.forms.models import model_to_dict
import json
from django.core import serializers as core_serializers




@database_sync_to_async
def gets_user():
    count = name.objects.all().values()
    print(list(count))
    return {
        "data" : list(count),
        "data2" : 'data'
    }