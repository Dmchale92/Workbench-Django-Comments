# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='ip',
            new_name='ip_address',
        ),
    ]