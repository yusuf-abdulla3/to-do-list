# Generated by Django 4.0.4 on 2023-03-12 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
