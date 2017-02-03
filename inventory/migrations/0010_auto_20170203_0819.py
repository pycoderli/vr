# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20170203_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='item_id',
            new_name='house_id',
        ),
    ]
