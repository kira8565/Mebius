# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20160719_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='model',
        ),
    ]
