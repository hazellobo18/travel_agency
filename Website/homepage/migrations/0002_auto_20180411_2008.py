# Generated by Django 2.0.3 on 2018-04-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]