# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171127_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
