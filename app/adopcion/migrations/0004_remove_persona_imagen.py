# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2022-09-03 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_persona_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='imagen',
        ),
    ]
