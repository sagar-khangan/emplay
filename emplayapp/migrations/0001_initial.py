# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-02 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField()),
                ('account_child_account', models.IntegerField()),
                ('potential', models.CharField(max_length=2)),
                ('pipeline', models.CharField(max_length=2)),
                ('stage', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Account_Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField()),
                ('account_name', models.CharField(max_length=250)),
                ('customer_name', models.CharField(max_length=250)),
                ('account_risk', models.TextField()),
            ],
        ),
    ]