# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_ongletsouverts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jeux',
            name='disponible',
        ),
    ]