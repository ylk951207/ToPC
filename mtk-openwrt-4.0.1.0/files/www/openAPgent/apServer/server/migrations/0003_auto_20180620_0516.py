# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_genericporttraffic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='genericporttraffic',
            name='id',
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='device_type',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='ip_addr',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='mac_addr',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='map_x',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='map_y',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='model_num',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='serial_num',
            field=models.CharField(default=-1, max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='status',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='user_id',
            field=models.CharField(default=-1, max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='user_passwd',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='vendor_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='vendor_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='device_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genericporttraffic',
            name='ifname',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
