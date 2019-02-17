from django.db import models
from tradgram.users import models as user_models
from tradgram.cases import models as case_models
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose

class CaseFile(models.Model):
    
    FILE_NAME = (
        ('위임 약정서','위임 약정서'),
        ('상표 등록 출원서','상표 등록 출원서'),
        ('의견 제출 통지서','의견 제출 통지서'),
        ('상표 등록증','상표 등록증'),
        ('기타 서류','기타 서류'),
    )
    
    # 주인이 사라졌을 때, 종속되어 있는 아이들을 어떻게 할것인가? 를 지정해 줘야 하는듯, on_delete=models.PROTECT를 넣어서 해결
    case = models.ForeignKey(case_models.Case, null=True, on_delete=models.PROTECT)
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    date_of_file = models.DateField(auto_now_add=True)
    file_page1 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50})
    file_page2 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    file_page3 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    file_page4 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    file_page5 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    file_name = models.CharField(max_length=80, choices=FILE_NAME, blank=True, null=True)