# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0025_auto_20170614_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeux',
            name='dateDeCreation',
            field=models.DateField(auto_now_add=True, verbose_name='Date de création'),
            preserve_default=False,
        ),
    ]