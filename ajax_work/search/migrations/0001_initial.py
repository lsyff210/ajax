# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=80, verbose_name='\u641c\u7d22\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u641c\u7d22\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u641c\u7d22\u5173\u952e\u8bcd',
            },
        ),
    ]