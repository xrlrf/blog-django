# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=5)),
                ('signature', models.CharField(max_length=80)),
            ],
        ),
    ]
