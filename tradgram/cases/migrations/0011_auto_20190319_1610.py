# Generated by Django 2.0.8 on 2019-03-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0010_auto_20190318_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='examiner_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='examiner_phone',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='examiner_team',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='expected_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='waiting_order',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='registration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
