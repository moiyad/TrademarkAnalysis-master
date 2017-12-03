# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171125_2005'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='phone_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
