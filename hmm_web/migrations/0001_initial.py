# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import hmm_web.model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_addr', models.TextField()),
                ('request_addr', models.TextField()),
                ('request_uri', models.TextField()),
                ('time', models.BigIntegerField(blank=True, default=hmm_web.model.current_time)),
                ('dangerous', models.NullBooleanField(default=False)),
            ],
        ),
    ]
