# Generated by Django 2.2.6 on 2019-12-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_auto_20191202_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskImage',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
