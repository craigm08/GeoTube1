# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTube', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawrequest',
            old_name='channel',
            new_name='Channel',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='dimensions',
            new_name='Dimensions',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='enddate',
            new_name='End_Date',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='fields',
            new_name='Fields',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='filters',
            new_name='Filters',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='maxresults',
            new_name='Max_Results',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='metrics',
            new_name='Metrics',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='sort',
            new_name='Sort',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='startdate',
            new_name='Start_Date',
        ),
        migrations.RenameField(
            model_name='rawrequest',
            old_name='startindex',
            new_name='Start_Index',
        ),
    ]
