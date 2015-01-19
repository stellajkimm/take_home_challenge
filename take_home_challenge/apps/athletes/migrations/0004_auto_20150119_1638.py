# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20141021_0605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='league',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name']},
        ),
    ]
