# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0002_auto_20180326_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='currrent_color',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='default_color',
        ),
        migrations.AddField(
            model_name='letter',
            name='cur_b',
            field=models.CharField(default='255', max_length=3),
        ),
        migrations.AddField(
            model_name='letter',
            name='cur_g',
            field=models.CharField(default='255', max_length=3),
        ),
        migrations.AddField(
            model_name='letter',
            name='cur_r',
            field=models.CharField(default='255', max_length=3),
        ),
        migrations.AddField(
            model_name='letter',
            name='def_b',
            field=models.CharField(default='255', max_length=3),
        ),
        migrations.AddField(
            model_name='letter',
            name='def_g',
            field=models.CharField(default='255', max_length=3),
        ),
        migrations.AddField(
            model_name='letter',
            name='def_r',
            field=models.CharField(default='255', max_length=3),
        ),
    ]