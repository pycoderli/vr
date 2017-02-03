# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20170203_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectedarrow',
            name='room_destination_id',
            field=models.CharField(max_length=100, default=1),
        ),
    ]
