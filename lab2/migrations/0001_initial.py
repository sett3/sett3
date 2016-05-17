# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clipography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=30)),
                ('album', models.CharField(max_length=30)),
                ('date', models.PositiveIntegerField()),
                ('director', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Discography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('year', models.PositiveIntegerField()),
                ('songs', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=30)),
                ('vocal', models.CharField(max_length=30)),
            ],
        ),
    ]
