# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0009_auto_20160520_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]