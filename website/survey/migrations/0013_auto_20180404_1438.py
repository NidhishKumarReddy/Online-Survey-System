# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_auto_20180404_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='userid',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]