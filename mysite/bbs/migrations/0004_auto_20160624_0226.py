# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20160624_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='usrname',
            new_name='user',
        ),
    ]
