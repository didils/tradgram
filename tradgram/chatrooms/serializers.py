from rest_framework import serializers
from . import models
from tradgram.users import models as user_models

class ChatRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChatRoom
        fields = (            
            'user1',
            'user2',
            'last_message',
            'new_message'
        )