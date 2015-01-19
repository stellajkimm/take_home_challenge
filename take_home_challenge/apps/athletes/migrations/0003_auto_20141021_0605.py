# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20141018_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='last_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='number',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='position',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='status',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
