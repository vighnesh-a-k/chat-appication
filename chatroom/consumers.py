# chat_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import authenticate, login






from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_group_name = None
        self.group_members = set()

    async def connect(self):
        print("WebSocket connected")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Add the channel to the list of group members
        self.group_members.add(self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Remove the channel from the list of group members
        self.group_members.discard(self.channel_name)

    async def receive(self, text_data):
       
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username= text_data_json["username"]
        print("Received:", text_data_json)
       
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'username':username,
            }
        )


    async def chat_message(self, event):
        print("Received chat message:", event)
        message = event['message']
        username=event['username']

        # Broadcast the message to the current user
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
