# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0007_auto_20160520_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
