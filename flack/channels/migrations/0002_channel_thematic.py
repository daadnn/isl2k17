# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='thematic',
            field=models.CharField(default='caca', max_length=100),
            preserve_default=False,
        ),
    ]
