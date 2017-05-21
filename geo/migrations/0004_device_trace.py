# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_auto_20170513_1933'),
        ('geo', '0003_auto_20170508_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Device')),
            ],
        ),
    ]