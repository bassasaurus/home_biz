# Generated by Django 3.0.8 on 2020-07-14 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20200711_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
