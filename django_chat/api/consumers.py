# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from .serializers import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        room = Room.objects.get_or_create(
            name = self.room_group_name
        )

        messages = Message.objects.filter(room=room[0])

        serializer = MessageSerializer(messages, many=True)

        serialized_messages = serializer.data

        self.room = room[0]
        self.messages = messages

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                'type': 'chat_message',
                'data': json.dumps({
                    'channel_name': self.channel_name,
                    'room_id': room[0].id,
                    'messages': serialized_messages
                })
            }
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']
        new_message = Message(
            message=data['message'],
            from_user=User.objects.get(id=data['from_user_id']),
            room=Room.objects.get(id=data['room_id']),
        )
        new_message.save()
        print(new_message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'data': json.dumps(data)
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'data': message
        }))