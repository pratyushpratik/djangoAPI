# Generated by Django 2.1.5 on 2019-02-27 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0033_auto_20190227_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetailtoday',
            name='today',
            field=models.CharField(default=datetime.datetime(2019, 2, 27, 13, 8, 34, 547641), max_length=100),
        ),
    ]
