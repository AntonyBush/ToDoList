<<<<<<< HEAD
# Generated by Django 3.1.2 on 2021-04-08 08:18

from django.db import migrations, models
import todo.models
=======
# Generated by Django 3.1.2 on 2021-04-07 14:25

from django.db import migrations, models
>>>>>>> 518bfbf55d5f1971203fc9f040edbd13603da752


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
<<<<<<< HEAD
            field=models.DateTimeField(default=todo.models.Task.default_start_time, null=True),
=======
            field=models.DateTimeField(null=True),
>>>>>>> 518bfbf55d5f1971203fc9f040edbd13603da752
        ),
    ]
