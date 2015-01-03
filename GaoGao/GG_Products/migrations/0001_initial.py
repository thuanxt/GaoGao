# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=255)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate_name', models.CharField(max_length=255)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='CategoryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate_detail_name', models.CharField(max_length=255)),
                ('cate_id', models.ForeignKey(to='GG_Products.Category')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_name', models.CharField(max_length=255)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loc_name', models.CharField(max_length=255)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('note', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_event', models.BooleanField(default=False)),
                ('brand_id', models.ForeignKey(to='GG_Products.Brand')),
                ('cate_detail_id', models.ForeignKey(to='GG_Products.CategoryDetail')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(max_digits=13, decimal_places=0)),
                ('color_id', models.ForeignKey(to='GG_Products.Color')),
                ('loc_id', models.ForeignKey(to='GG_Products.Location')),
                ('product_id', models.ForeignKey(to='GG_Products.Product')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
