from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ChatRoom)
class ChatroomsAdmin(admin.ModelAdmin):

    search_fields =(
        'user1',
        'user2',
        'last_message',
        'new_message'
    )
    
    list_filter = (
        'user1',
        'user2',
        'last_message',
        'new_message'
    )

    list_display = (
        'user1',
        'user2',
        'last_message',
        'new_message'
    )