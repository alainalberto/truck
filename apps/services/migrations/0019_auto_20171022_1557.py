# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20171021_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='cargo_policy',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='physical_damg_policy',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]