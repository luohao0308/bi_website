# Generated by Django 3.2.4 on 2021-07-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(editable=False, max_length=12, verbose_name='查询记录ID')),
                ('conditions', models.TextField(blank=True, null=True, verbose_name='查询条件')),
                ('objs', models.ManyToManyField(blank=True, to='dashboard.Order')),
            ],
            options={
                'verbose_name': '查询记录',
            },
        ),
    ]
