# Generated by Django 2.0.8 on 2018-11-04 17:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_auto_20181105_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='applicantArray',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='paymentArray',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]