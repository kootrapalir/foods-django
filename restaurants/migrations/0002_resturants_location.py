# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturants',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
