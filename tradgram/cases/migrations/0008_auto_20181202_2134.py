# Generated by Django 2.0.8 on 2018-12-02 12:34

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_case_identification_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='file',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
    ]