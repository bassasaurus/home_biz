# Generated by Django 3.0.8 on 2020-07-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20200718_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=6),
        ),
    ]
