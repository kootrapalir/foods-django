# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20171127_1824'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResturantLocation',
            new_name='RestaurantLocation',
        ),
    ]