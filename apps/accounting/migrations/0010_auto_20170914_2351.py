# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_auto_20170830_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='start_date',
            field=models.DateField(default='2017-09-14'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='start_date',
            field=models.DateField(default='2017-09-14'),
        ),
    ]