# Generated by Django 3.0 on 2020-01-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200109_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='fleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fromdate', models.DateField(max_length=10)),
                ('todate', models.DateField(max_length=10)),
                ('reason', models.CharField(max_length=30)),
            ],
        ),
    ]