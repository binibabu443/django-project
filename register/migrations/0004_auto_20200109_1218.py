# Generated by Django 3.0 on 2020-01-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200109_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmark',
            old_name='stdid',
            new_name='sid',
        ),
    ]