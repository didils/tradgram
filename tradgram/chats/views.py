from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from django.db.models import Q

class ListAllChats(APIView):

    def get(self, request, format=None):

        user = request.query_params.get('searchName', None)
        
        all_chats = models.Chat.objects.filter(Q(sender_username=user) | Q(receiver_username=user))

        serializer = serializers.ChatSerializer(all_chats, many=True, context={'request': request})

        """
        Serializer로 serialize할 때, 동일한 모델을 serialize하는 serializer를 사용해야만 함.
        
        여기서, all_cases는 models.Case이고,
        CaseSerialize 역시 models.Case를 씨리얼라이즈하고 있으(serializer.py참조)므로 가능
        """

        return Response(data=serializer.data)

class UploadChats(APIView):

    def post(self, request, format=None):

        serializer = serializers.ChatUploadSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       