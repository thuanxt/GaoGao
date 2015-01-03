# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GG_Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productdetail',
            unique_together=set([('product_id', 'color_id', 'loc_id')]),
        ),
    ]
