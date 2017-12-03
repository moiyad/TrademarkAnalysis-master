# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Business company', b'1'), (b'Guest User', b'2'), (b'Law firm office', b'3')]),
        ),
    ]
