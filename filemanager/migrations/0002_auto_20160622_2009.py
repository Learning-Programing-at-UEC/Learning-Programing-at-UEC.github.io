# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTypeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_datatype', models.CharField(max_length=10)),
                ('new_datatype_ID', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='datafile',
            name='data',
            field=models.FileField(upload_to='files'),
        ),
    ]
