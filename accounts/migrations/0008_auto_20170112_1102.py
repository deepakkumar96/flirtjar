# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170110_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
