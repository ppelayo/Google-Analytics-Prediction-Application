# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20170322_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_rf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_data_json', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='dog',
        ),
    ]
