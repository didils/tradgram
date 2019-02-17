from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):

    search_fields =(
        'sender_username',
        'receiver_username',
        'createdAt',
        'text',
        '_id'
    )
    
    list_filter = (
        'sender_username',
        'receiver_username',
        'createdAt',
        'text',
        '_id'
    )