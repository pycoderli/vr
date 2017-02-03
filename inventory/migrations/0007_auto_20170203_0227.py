# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectedarrow',
            name='position',
            field=models.CharField(max_length=100, default='0 0 0'),
        ),
        migrations.AddField(
            model_name='connectedarrow',
            name='rotation',
            field=models.CharField(max_length=100, default='0 0 0'),
        ),
    ]
