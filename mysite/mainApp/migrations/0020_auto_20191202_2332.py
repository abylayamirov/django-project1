# Generated by Django 2.2.6 on 2019-12-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_auto_20191130_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='ioImage',
            field=models.ImageField(default='/static/mainApp/img/iodefault.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='task',
            name='taskImage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
