# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20150703_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='tree_parent',
            field=models.ForeignKey(related_name='children', blank=True, to='locations.Location', null=True),
        ),
    ]
