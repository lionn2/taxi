# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0002_auto_20150113_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conditioner', models.BooleanField(default=False)),
                ('type_salon', models.IntegerField(default=0)),
                ('place_from_things', models.BooleanField(default=False)),
                ('count_places', models.IntegerField(default=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='driveruser',
            name='add_service',
            field=models.OneToOneField(default=None, to='taxi_app.AddService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driveruser',
            name='date_registration',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driveruser',
            name='rate_without_client',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='add_service',
            field=models.OneToOneField(default=None, to='taxi_app.AddService'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientuser',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='driveruser',
            name='photo_car',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='driveruser',
            name='photo_car_license',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='driveruser',
            name='photo_driver_license',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='building',
            field=models.CharField(default=b'', max_length=5, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='x',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='y',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
