from django.conf.urls import url
from . import views

app_name = "chats"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllChats.as_view(),
        name='all_chats'
    ),
    url(
        regex=r'^upload/$',
        view=views.UploadChats.as_view(),
        name='upload_chat'
    )
]