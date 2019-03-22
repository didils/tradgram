from rest_framework import serializers
from . import models
from tradgram.users import models as user_models
from tradgram.cases import models as case_models


class CaseFileUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class CaseFileCaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = case_models.Case
        fields = (
            'trademark_title',
            'application_number',
            'identification_number'
        )

class CaseFileSerializer(serializers.ModelSerializer):

    owner = CaseFileUserSerializer()
    case = CaseFileCaseSerializer()
    
    class Meta:
        model = models.CaseFile
        fields = (
            'case',
            'owner',
            'date_of_file',
            # 'file_page1',
            # 'file_page2',
            # 'file_page3',
            # 'file_page4',
            # 'file_page5',
            'file_name',
            'file_pdf'
        )