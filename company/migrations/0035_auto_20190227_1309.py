# Generated by Django 2.1.5 on 2019-02-27 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0034_auto_20190227_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetailtoday',
            name='today',
            field=models.CharField(default=datetime.datetime(2019, 2, 27, 13, 9, 57, 160910), max_length=100),
        ),
    ]
