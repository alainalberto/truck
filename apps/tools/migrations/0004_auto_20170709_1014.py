# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20170628_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.FileField(blank=True, null=True, upload_to='Forms/'),
        ),
    ]
