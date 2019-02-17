from django.db import models
from tradgram.users import models as user_models

# Create your models here.

class Chat(models.Model):
    
    # 주인이 사라졌을 때, 종속되어 있는 아이들을 어떻게 할것인가? 를 지정해 줘야 하는듯, on_delete=models.PROTECT를 넣어서 해결
    sender_username = models.CharField(max_length=80, null=True, blank=True)
    receiver_username = models.CharField(max_length=80, null=True, blank=True)
    createdAt = models.CharField(max_length=80, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    _id = models.CharField(max_length=80, null=True, blank=True)