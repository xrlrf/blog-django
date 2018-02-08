# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubHeader',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='article.Publisher')),
                ('url', models.FileField(upload_to=b'pubheader')),
            ],
        ),
    ]
