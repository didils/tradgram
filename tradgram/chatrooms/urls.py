from django.conf.urls import url
from . import views

app_name = "chatrooms"

urlpatterns = [
    url(
        regex=r'^upload/$',
        view=views.UploadChatRooms.as_view(),
        name='upload_chatrooms'
    ),
    url(
        regex=r'^all/$',
        view=views.ListAllChatRooms.as_view(),
        name='all_chatrooms'
    )
]