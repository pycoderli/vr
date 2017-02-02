# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(default='https://raw.githubusercontent.com/aframevr/aframe/master/examples/boilerplate/panorama/puydesancy.jpg'),
        ),
    ]
