# Generated by Django 2.0.3 on 2018-04-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20180412_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculateprice',
            name='adult',
            field=models.IntegerField(default=0),
        ),
    ]
