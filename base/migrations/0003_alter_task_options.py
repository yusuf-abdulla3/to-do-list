# Generated by Django 4.0.4 on 2023-03-13 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
    ]
