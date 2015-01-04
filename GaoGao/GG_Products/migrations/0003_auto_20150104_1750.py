# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GG_Products', '0002_auto_20150103_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorydetail',
            name='cate_id',
        ),
        migrations.AddField(
            model_name='category',
            name='cate_parent_id',
            field=models.ForeignKey(default=1, to='GG_Products.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cate_detail_id',
            field=models.ForeignKey(to='GG_Products.Category'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='CategoryDetail',
        ),
    ]
