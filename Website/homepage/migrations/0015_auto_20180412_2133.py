# Generated by Django 2.0.3 on 2018-04-12 16:03

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_auto_20180412_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.CharField(blank=True, max_length=10, verbose_name=django.contrib.auth.models.User),
        ),
    ]