# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150328_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('logo', models.CharField(max_length=300, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Leagues',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(related_name=b'teams', to='app.League', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='linkToRoster',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='team',
            name='ballpark',
            field=models.CharField(default=b'', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='hometown',
            field=models.CharField(default=b'', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='manager',
            field=models.CharField(default=b'', max_length=50, null=True),
        ),
    ]
