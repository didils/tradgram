# Generated by Django 2.0.8 on 2019-03-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190321_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
