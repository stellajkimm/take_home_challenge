# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20141017_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='league',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='athlete',
            old_name='sport',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='athlete',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(to='athletes.Team'),
        ),
    ]
