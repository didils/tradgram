# Generated by Django 2.0.8 on 2019-03-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190321_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fcm_pushtoken',
            field=models.TextField(blank=True, null=True),
        ),
    ]
