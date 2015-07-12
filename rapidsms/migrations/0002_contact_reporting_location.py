# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20150703_0840'),
        ('rapidsms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reporting_location',
            field=models.ForeignKey(blank=True, to='locations.Location', null=True),
        ),
    ]
