# Generated by Django 3.2.6 on 2021-10-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTH_SYSTEM', '0002_auto_20211006_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]