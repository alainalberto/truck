# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companie',
            name='ein',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='companie',
            name='fax',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='companie',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]