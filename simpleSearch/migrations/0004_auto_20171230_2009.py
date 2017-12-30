# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-30 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleSearch', '0003_trademarkmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trademarkmodel',
            name='image',
        ),
        migrations.AddField(
            model_name='trademarkmodel',
            name='Image',
            field=models.ImageField(null=True, upload_to='./media/'),
        ),
        migrations.AddField(
            model_name='trademarkmodel',
            name='Owner_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='trademarkmodel',
            name='Trademark_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]