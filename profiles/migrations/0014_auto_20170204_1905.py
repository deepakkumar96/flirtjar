# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0013_auto_20170112_1859'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usermatch',
            unique_together=set([('user_to', 'user_from')]),
        ),
    ]