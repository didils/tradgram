# Generated by Django 2.0.8 on 2019-03-31 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_push_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='push_token',
        ),
    ]
