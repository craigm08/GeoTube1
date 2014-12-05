# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTube', '0002_auto_20141113_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50, verbose_name=b'User name')),
                ('following', models.IntegerField(verbose_name=b'Following ', blank=True)),
                ('address', models.IntegerField(verbose_name=b'Point address', blank=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'User Input',
            },
            bases=(models.Model,),
        ),
    ]
