# Generated by Django 3.1.2 on 2021-04-07 16:03

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210407_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=todo.models.Task.default_start_time),
        ),
    ]
