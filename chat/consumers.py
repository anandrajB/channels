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
from .query import gets_user

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'
        print('connected')
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
    
   

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = text_data_json['user_id']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'send_notification',
                'user_id':user_id,
            }
        )

    async def send_notification(self, event):
        user_id = event['user_id']
        print(user_id)
        data = await gets_user()
        await self.send(text_data=json.dumps({
            'type':'chat',
            'user_id':user_id,
            'my_case' : 'hul',
            'some_data' : data,
        }))



