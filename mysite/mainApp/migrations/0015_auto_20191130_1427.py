# Generated by Django 2.2.7 on 2019-11-30 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_remove_task_fulldescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='shortdescription',
            new_name='description',
        ),
    ]
