# Generated by Django 2.0.8 on 2019-03-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseFiles', '0008_casefile_isreportexist'),
    ]

    operations = [
        migrations.AddField(
            model_name='casefile',
            name='expireDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
