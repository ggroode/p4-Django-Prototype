from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class BasicConsumer(WebsocketConsumer):
    identifier = 'all'
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.identifier,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.identifier,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.identifier,
            {
                'type': 'chat_message',
                'message': text_data
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=message)

class SetupConsumer(BasicConsumer):
    identifier='setup'
class PlayConsumer(BasicConsumer):
    identifier='play'
