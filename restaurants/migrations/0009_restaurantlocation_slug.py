# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20171127_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
