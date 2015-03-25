# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name=b'Player', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]
