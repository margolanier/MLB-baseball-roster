# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150325_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='owner',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name=b'players', to='app.Team'),
        ),
    ]
