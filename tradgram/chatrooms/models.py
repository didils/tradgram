from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    
    user1 = models.CharField(max_length=80, null=True, blank=True)
    user2 = models.CharField(max_length=80, null=True, blank=True)
    last_message = models.CharField(max_length=80, null=True, blank=True)
    new_message = models.BooleanField(default=True)