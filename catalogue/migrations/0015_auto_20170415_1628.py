# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0014_auto_20170414_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeux',
            name='image',
            field=models.ImageField(null=True, upload_to='photos_jeux/', verbose_name='Image'),
        ),
    ]
