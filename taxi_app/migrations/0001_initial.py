# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rate', models.FloatField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('date_registration', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('whom', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(to='taxi_app.ClientUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DriverRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_state', models.IntegerField()),
                ('order_execution', models.IntegerField()),
                ('comfort', models.IntegerField()),
                ('avarage_value', models.FloatField()),
                ('client', models.ForeignKey(to='taxi_app.ClientUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DriverUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo_car', models.ImageField(upload_to=b'')),
                ('photo_driver_license', models.ImageField(upload_to=b'')),
                ('photo_car_license', models.ImageField(upload_to=b'')),
                ('rate_min', models.IntegerField()),
                ('rate_km_hightway', models.IntegerField()),
                ('rate_km_city', models.IntegerField()),
                ('about_me', models.TextField()),
                ('coefficient_congestion', models.FloatField(default=1)),
                ('state', models.IntegerField()),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('cost', models.FloatField()),
                ('state', models.IntegerField()),
                ('time_travel', models.IntegerField()),
                ('long_travel', models.IntegerField()),
                ('is_fast', models.BooleanField(default=True)),
                ('client', models.ForeignKey(to='taxi_app.ClientUser')),
                ('client_rating', models.OneToOneField(to='taxi_app.ClientRating')),
                ('driver', models.ForeignKey(to='taxi_app.DriverUser')),
                ('driver_rating', models.OneToOneField(to='taxi_app.DriverRating')),
                ('end_location', models.OneToOneField(related_name='end_location', to='taxi_app.Location')),
                ('start_location', models.OneToOneField(related_name='start_location', to='taxi_app.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_orders', models.IntegerField()),
                ('count_drivings', models.IntegerField()),
                ('on_app', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='driveruser',
            name='location',
            field=models.OneToOneField(to='taxi_app.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driverrating',
            name='driver',
            field=models.ForeignKey(to='taxi_app.DriverUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='driver',
            field=models.ForeignKey(to='taxi_app.DriverUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='order',
            field=models.ForeignKey(to='taxi_app.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientuser',
            name='favourite_drivers',
            field=models.ManyToManyField(to='taxi_app.DriverUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrating',
            name='client',
            field=models.ForeignKey(to='taxi_app.ClientUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrating',
            name='driver',
            field=models.ForeignKey(to='taxi_app.DriverUser'),
            preserve_default=True,
        ),
    ]
