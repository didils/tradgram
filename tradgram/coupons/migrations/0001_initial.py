# Generated by Django 2.0.8 on 2019-03-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('discount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('coupon_name', models.CharField(blank=True, max_length=80, null=True)),
                ('coupon_type', models.CharField(blank=True, choices=[('비율할인', '비율할인'), ('원플러스원', '원플러스원'), ('금액할인', '금액할인')], max_length=80, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
