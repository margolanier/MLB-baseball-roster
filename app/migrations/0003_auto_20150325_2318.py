# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150325_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='ballpark',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='championships',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='hometown',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='manager',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
