# Generated by Django 2.2.7 on 2019-11-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20191130_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='f_description',
            field=models.TextField(default=None, max_length=2000, verbose_name='Полное описание задачи'),
        ),
        migrations.AddField(
            model_name='task',
            name='s_description',
            field=models.TextField(default=None, max_length=200, verbose_name='Наименование задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='topic',
            field=models.CharField(default=None, max_length=200, verbose_name='Название темы'),
        ),
    ]