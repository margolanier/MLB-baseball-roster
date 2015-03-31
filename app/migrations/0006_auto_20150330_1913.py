# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150330_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='ballpark',
        ),
        migrations.RemoveField(
            model_name='team',
            name='championships',
        ),
        migrations.RemoveField(
            model_name='team',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='team',
            name='manager',
        ),
    ]
