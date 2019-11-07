# Generated by Django 2.2.7 on 2019-11-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=27)),
                ('attending', models.CharField(max_length=3)),
                ('not_attending', models.CharField(default='N/A', max_length=100)),
                ('favourite_song', models.CharField(max_length=100)),
                ('dietary_requirements', models.CharField(default='N/A', max_length=100)),
                ('additional_info', models.TextField(default='N/A', max_length=2000)),
            ],
        ),
    ]