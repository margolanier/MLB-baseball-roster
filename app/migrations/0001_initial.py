# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(unique=True)),
                ('batsthrows', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('birthday', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('number', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name=b'players', to='app.Team'),
            preserve_default=True,
        ),
    ]
