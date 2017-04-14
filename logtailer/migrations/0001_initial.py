# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='name')),
                ('regex', models.CharField(max_length=500, verbose_name='regex')),
            ],
            options={
                'verbose_name': 'filter',
                'verbose_name_plural': 'filters',
            },
        ),
        migrations.CreateModel(
            name='LogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='name')),
                ('path', models.CharField(max_length=500, verbose_name='path')),
            ],
            options={
                'verbose_name': 'log_file',
                'verbose_name_plural': 'log_files',
            },
        ),
        migrations.CreateModel(
            name='LogsClipboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('logs', models.TextField(verbose_name='logs')),
                ('log_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logtailer.LogFile', verbose_name='log_file')),
            ],
            options={
                'verbose_name': 'logs_clipboard',
                'verbose_name_plural': 'logs_clipboard',
            },
        ),
    ]
