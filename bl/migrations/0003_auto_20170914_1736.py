# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0002_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
