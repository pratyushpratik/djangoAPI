# Generated by Django 2.1.5 on 2019-02-22 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20190125_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetailtoday',
            name='today',
            field=models.CharField(default=datetime.datetime(2019, 2, 22, 12, 51, 26, 634072), max_length=100),
        ),
    ]