# Generated by Django 2.0.8 on 2019-03-25 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Point_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.CharField(blank=True, max_length=80, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('change_amount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('use_status', models.CharField(blank=True, choices=[('적립', '적립'), ('사용', '사용')], max_length=80, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]