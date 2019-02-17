from rest_framework import serializers
from . import models
from tradgram.users import models as user_models

class ChatUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class ChatSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Chat
        fields = (            
            'sender_username',
            'receiver_username',
            'createdAt',
            'text',
            '_id'
        )

class ChatUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = (
            'sender_username',
            'receiver_username',
            'createdAt',
            'text',
            '_id'
        )