# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='event',
        ),
        migrations.AddField(
            model_name='presentation',
            name='event',
            field=models.ManyToManyField(blank=True, to='website.Event'),
        ),
    ]
