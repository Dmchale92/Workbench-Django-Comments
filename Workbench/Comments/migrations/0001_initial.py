# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('content_url', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]