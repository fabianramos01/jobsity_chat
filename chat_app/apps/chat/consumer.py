from datetime import datetime
from re import compile

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from json import dumps, loads

from apps.chat.models import Message, Room
from apps.users.models import CustomUser

pattern_stock = compile(r'^/stock=.*')

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data_json = loads(text_data)
        if pattern_stock.match(data_json['message']) or (data_json['owner'] == 'bot' and 'Error' in data_json['message']):
            timestamp = datetime.utcnow()
        else:
            message = await new_message(self.room_group_name, data_json)
            timestamp = message.timestamp
        data_json['timestamp'] = timestamp.strftime('%b. %d, %Y, %I:%M %p').replace('AM', 'am').replace('PM', 'pm')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'content': data_json
            }
        )

    async def send_message(self, event):
        await self.send(
            text_data=dumps(event['content'])
        )

@database_sync_to_async
def new_message(room, data):
    return Message.objects.create(room=Room.objects.get(name=room), content=data['message'], owner=CustomUser.objects.get(username=data['owner']))
