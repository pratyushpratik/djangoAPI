# Generated by Django 2.1.5 on 2019-02-27 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20190227_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetailtoday',
            name='today',
            field=models.CharField(default=datetime.datetime(2019, 2, 27, 7, 27, 5, 984828), max_length=100),
        ),
    ]
