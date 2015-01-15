# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientuser',
            old_name='rate',
            new_name='rating',
        ),
    ]
