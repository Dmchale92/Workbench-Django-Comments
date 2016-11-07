# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0003_remove_comment_content_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content_url',
            field=models.SlugField(default='planetary-motion'),
            preserve_default=False,
        ),
    ]
