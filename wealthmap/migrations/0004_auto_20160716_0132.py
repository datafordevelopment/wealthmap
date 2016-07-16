# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wealthmap', '0003_auto_20160715_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='phone')),
                ('fax', models.CharField(blank=True, max_length=255, verbose_name='fax')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('street_address', models.TextField(blank=True, verbose_name='street address')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='url')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name_plural': 'Agencies',
                'verbose_name': 'Agency',
            },
        ),
        migrations.AddField(
            model_name='opportunity',
            name='agency',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='wealthmap.Agency', verbose_name='agency'),
            preserve_default=False,
        ),
    ]