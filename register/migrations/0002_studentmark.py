# Generated by Django 3.0.2 on 2020-01-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('assessmentno', models.IntegerField(blank=True, null=True)),
                ('sub1mark', models.IntegerField(blank=True, null=True)),
                ('sub2mark', models.IntegerField(blank=True, null=True)),
                ('sub3mark', models.IntegerField(blank=True, null=True)),
                ('percentage', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
