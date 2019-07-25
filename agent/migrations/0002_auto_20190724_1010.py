# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-24 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_hash',
        ),
        migrations.AlterField(
            model_name='tenant',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='id_number',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]