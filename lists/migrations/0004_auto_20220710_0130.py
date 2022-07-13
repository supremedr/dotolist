# Generated by Django 2.2.2 on 2022-07-10 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_item_lista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=500)),
                ('periority', models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')])),
                ('timing', models.DateTimeField(default=datetime.datetime(2022, 7, 10, 1, 30, 30, 685125, tzinfo=utc))),
                ('done', models.BooleanField(default=False)),
                ('lista', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='lists.Lista')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
