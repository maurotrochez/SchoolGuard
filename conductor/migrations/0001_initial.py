# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('idConductor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('paseConduccion', models.CharField(max_length=10)),
            ],
        ),
    ]
