# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GG_Products', '0004_auto_20150104_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
