from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from django.db.models import Q

class ListAllChatRooms(APIView):

    def get(self, request, format=None):

        user = request.query_params.get('username', None)        
        
        all_chatrooms = models.ChatRoom.objects.filter(Q(user1 = user) | Q(user2 = user))

        serializer = serializers.ChatRoomSerializer(all_chatrooms, many=True, context={'request': request})

        return Response(data=serializer.data)

class UploadChatRooms(APIView):

    def post(self, request, format=None):

        user1 = 'didils'
        user2 = request.query_params.get('username', None) 

        all_chatroom = models.ChatRoom.objects.all()

        if all_chatroom.filter(user1=user1, user2=user2):                    
                    print('이미 대화방 존재함')

        elif all_chatroom.filter(user1=user1, user2=user2):
                    print('이미 대화방 존재함')
                    
        else:
                    models.ChatRoom.objects.create(user1=user1, user2=user2)
                    print(user1, '과', user2, '의 대화방을 새로 생성!')

        return Response(status=status.HTTP_201_CREATED)