# Generated by Django 2.2.7 on 2019-11-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_auto_20191130_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='f_description',
            new_name='fulldescription',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='s_description',
            new_name='shortdescription',
        ),
    ]
