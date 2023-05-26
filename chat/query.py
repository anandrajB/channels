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
from asgiref.sync import sync_to_async
import asyncio
from dataclasses import dataclass
from django.db.models import Sum
import json


@dataclass
class datacs:

    def gg(self):
        return  {
            "data3333" : name.objects.aggregate(Sum('amount')).get('amount__sum'),
            'data222' : name.objects.aggregate(Sum('amount')).get('amount__sum')
        }
    
    
    def gets_some(self):
        data =  name.objects.all().values('id','amount')
        rs = []
        for i in data:
            core = {
                'iter' : i['id']
            }
            rs.append(core)
        return rs


    @database_sync_to_async
    def ff(self):
        return {
            "data" : list(name.objects.values('id','username')),
            "data1" : list(name.objects.values('id','username')),
            "data2" : name.objects.values().count(),
            "amount" : name.objects.aggregate(Sum('amount')).get('amount__sum')
        }

    @database_sync_to_async
    def base_core(self):
        return {
            "core" : self.gg(),
            'get' : self.gets_some(),
            "data" : name.objects.aggregate(Sum('amount')).get('amount__sum')
        }


    async def gets_user(self):
        return await self.base_core()

    async def gets_dash(self):
        return await self.ff()
        



# @database_sync_to_async
# def gets_user():
#     count = name.objects.all().values()
#     print(list(count))
#     return {
#         "data" : list(count),
#         "data2" : 'data'
#     }