# Generated by Django 3.2.3 on 2021-05-23 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
