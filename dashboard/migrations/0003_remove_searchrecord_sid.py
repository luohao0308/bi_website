# Generated by Django 3.2.4 on 2021-07-23 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_searchrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchrecord',
            name='sid',
        ),
    ]
