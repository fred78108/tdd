# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20180114_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
    ]
