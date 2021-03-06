# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-09 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterField(
            model_name='structure',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structures.Region', verbose_name='region'),
        ),
    ]
