# Generated by Django 2.0.8 on 2018-11-04 17:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20181031_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='product_comment',
            new_name='descriptions',
        ),
        migrations.AddField(
            model_name='case',
            name='designatedArray',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
