# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2022-09-01 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20220901_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='folio',
        ),
        migrations.AddField(
            model_name='mascota',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
