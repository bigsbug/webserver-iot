# Generated by Django 3.2.5 on 2021-07-11 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demo_webserver_app', '0004_auto_20210711_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='create',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='newstatus',
            old_name='create',
            new_name='date',
        ),
    ]
