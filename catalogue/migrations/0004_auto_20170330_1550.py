# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-30 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20170330_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietaire',
            name='user',
        ),
        migrations.AlterField(
            model_name='jeux',
            name='dureeMax',
            field=models.IntegerField(verbose_name='Dur\xe9e maximum'),
        ),
    ]
