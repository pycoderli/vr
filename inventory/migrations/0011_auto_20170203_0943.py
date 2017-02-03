# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20170203_0819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
