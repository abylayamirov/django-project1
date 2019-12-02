# Generated by Django 2.2.7 on 2019-11-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_auto_20191130_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='s_description',
        ),
        migrations.AddField(
            model_name='task',
            name='f_description',
            field=models.TextField(default='Fully', max_length=1000, verbose_name='Описание задачи'),
        ),
    ]
