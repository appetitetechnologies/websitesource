# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('abstract', models.CharField(max_length=1200)),
                ('cid', models.IntegerField()),
            ],
        ),
    ]
