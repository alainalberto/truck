# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companie',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
