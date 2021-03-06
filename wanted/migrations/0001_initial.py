# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('contact_person', models.CharField(max_length=100)),
                ('apply_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
