# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-28 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trademark',
            name='me',
            field=models.CharField(default='hi', max_length=255),
        ),
    ]
