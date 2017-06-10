# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 21:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Busines'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.File'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='accounts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account'),
        ),
        migrations.AddField(
            model_name='payment',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Busines'),
        ),
        migrations.AddField(
            model_name='payment',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoiceshasitem',
            name='invoices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Invoice'),
        ),
        migrations.AddField(
            model_name='invoiceshasitem',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='accounts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Busines'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Customer'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fee',
            name='accounts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account'),
        ),
        migrations.AddField(
            model_name='employeehaspayment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Employee'),
        ),
        migrations.AddField(
            model_name='employeehaspayment',
            name='payments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Payment'),
        ),
        migrations.AddField(
            model_name='employee',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Busines'),
        ),
        migrations.AddField(
            model_name='customer',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Busines'),
        ),
        migrations.AddField(
            model_name='customer',
            name='folders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Folder'),
        ),
        migrations.AddField(
            model_name='customer',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accountdescrip',
            name='accounts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Account'),
        ),
        migrations.AddField(
            model_name='accountdescrip',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='accounts_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]