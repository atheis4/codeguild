# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0010_auto_20160520_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]