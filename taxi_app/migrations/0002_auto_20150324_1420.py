# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientuser',
            name='is_authorized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driveruser',
            name='is_authorized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
