# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bloguser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='type',
            field=models.CharField(default='1', max_length=255, choices=[(b'1', b'Business company'), (b'2', b'Guest User'), (b'3', b'Law firm office')]),
            preserve_default=False,
        ),
    ]
