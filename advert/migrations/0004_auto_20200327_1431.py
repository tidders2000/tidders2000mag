# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-27 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20200327_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='contact_telephone',
            field=models.CharField(default='', max_length=254),
        ),
    ]
