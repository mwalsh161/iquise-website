# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-29 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180827_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenter',
            name='profile_image_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image_url',
        ),
        migrations.AddField(
            model_name='presenter',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='presenters'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='staff_profiles'),
        ),
    ]
