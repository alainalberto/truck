# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_auto_20170829_1843'),
        ('services', '0014_auto_20170820_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='companies',
        ),
        migrations.AddField(
            model_name='driver',
            name='customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.Customer'),
        ),
        migrations.AddField(
            model_name='driver',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
