# Generated by Django 3.0.6 on 2020-05-25 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200525_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='cert_recieved',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 58, 54, 395214), verbose_name='date recieved'),
        ),
    ]
