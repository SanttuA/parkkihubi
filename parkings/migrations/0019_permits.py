# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-14 10:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models

from ..fields import CleaningJsonField
from ..validators import DictListValidator, TextField, TimestampField


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0018_parking_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='time modified')),
                ('external_id', models.CharField(blank=True, max_length=50, null=True)),
                ('subjects', CleaningJsonField(validators=[
                    DictListValidator({
                        'start_time': TimestampField(),
                        'end_time': TimestampField(),
                        'registration_number': TextField(max_length=20),
                    })])),
                ('areas', CleaningJsonField(validators=[
                    DictListValidator({
                        'start_time': TimestampField(),
                        'end_time': TimestampField(),
                        'area': TextField(max_length=10),
                    })])),
            ],
            options={
                'ordering': ('series', 'id'),
            },
        ),
        migrations.CreateModel(
            name='PermitCacheItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=30)),
                ('area_identifier', models.CharField(max_length=10)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('permit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cache_items', to='parkings.Permit')),
            ],
        ),
        migrations.CreateModel(
            name='PermitSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='time modified')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.AddField(
            model_name='permit',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parkings.PermitSeries'),
        ),
        migrations.AddIndex(
            model_name='permit',
            index=models.Index(fields=['series', 'id'], name='parkings_pe_series__19e6e5_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='permit',
            unique_together=set([('series', 'external_id')]),
        ),
    ]
