# Generated by Django 2.0.8 on 2019-03-23 06:35

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('OAreports', '0002_auto_20190323_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oareport',
            name='image1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='oareport',
            name='image2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='oareport',
            name='image3',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='oareport',
            name='image4',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='oareport',
            name='image5',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
    ]
