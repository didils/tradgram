# Generated by Django 2.0.8 on 2018-09-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.IntegerField(null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('product_en', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
