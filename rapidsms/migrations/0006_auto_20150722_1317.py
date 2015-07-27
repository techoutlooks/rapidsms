# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidsms', '0005_message_transmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='in_response_to',
        ),
        migrations.RemoveField(
            model_name='transmission',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='transmission',
            name='message',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Transmission',
        ),
    ]
