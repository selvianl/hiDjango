# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-25 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milyoncu', '0008_auto_20190221_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
