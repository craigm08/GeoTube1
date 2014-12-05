# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=75)),
                ('startdate', models.CharField(max_length=50)),
                ('enddate', models.CharField(max_length=50)),
                ('metrics', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('filters', models.CharField(max_length=100)),
                ('maxresults', models.CharField(max_length=50)),
                ('sort', models.CharField(max_length=50)),
                ('startindex', models.CharField(max_length=50)),
                ('fields', models.CharField(max_length=50)),
                ('Status', models.CharField(default=b'Submitted', max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
