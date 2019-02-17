from django.conf.urls import url
from . import views

app_name = "caseFiles"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllCaseFiles.as_view(),
        name='all_case_files'
    ),
    url(
        regex=r'^upload/$',
        view=views.UploadCaseFiles.as_view(),
        name='upload_case_files'
    )
]