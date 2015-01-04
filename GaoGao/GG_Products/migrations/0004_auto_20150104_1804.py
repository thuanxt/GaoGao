# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GG_Products', '0003_auto_20150104_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cate_parent_id',
            field=models.ForeignKey(blank=True, to='GG_Products.Category', null=True),
            preserve_default=True,
        ),
    ]
