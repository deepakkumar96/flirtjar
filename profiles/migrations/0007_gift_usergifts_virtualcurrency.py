# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0006_auto_20170102_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(verbose_name=b'The price of the gift in terms of VirtualCurrency.')),
                ('icon', models.ImageField(upload_to=b'gifts')),
            ],
        ),
        migrations.CreateModel(
            name='UserGifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Gift')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VirtualCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
