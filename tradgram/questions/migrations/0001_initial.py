# Generated by Django 2.0.8 on 2019-04-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(blank=True, max_length=140, null=True)),
                ('category', models.CharField(blank=True, choices=[('어플 사용 관련', '어플 사용 관련'), ('변리사/특허법인 관련', '변리사/특허법인 관련'), ('특허/디자인 업무 관련', '특허/디자인 업무 관련'), ('해외 출원 관련', '해외 출원 관련'), ('상표 출원 전반', '상표 출원 전반'), ('비용 관련', '비용 관련'), ('기타', '기타')], max_length=80, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('question_detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
