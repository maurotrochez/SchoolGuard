# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colegio',
            name='idColegio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
