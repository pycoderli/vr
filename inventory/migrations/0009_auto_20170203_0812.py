# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_connectedarrow_room_destination_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='House',
        ),
    ]
