# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='lat_end',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='long_end',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]