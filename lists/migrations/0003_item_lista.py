# Generated by Django 2.2.2 on 2022-07-08 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lista',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='lists.Lista'),
            preserve_default=False,
        ),
    ]
