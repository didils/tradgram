# Generated by Django 2.0.8 on 2018-11-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20181129_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='createdAt',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
