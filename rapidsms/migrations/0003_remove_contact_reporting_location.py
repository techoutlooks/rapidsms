# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidsms', '0002_contact_reporting_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='reporting_location',
        ),
    ]
