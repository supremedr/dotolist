# Generated by Django 2.2.2 on 2022-07-10 03:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20220710_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterField(
            model_name='task',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 3, 21, 1, 446257, tzinfo=utc)),
        ),
    ]
