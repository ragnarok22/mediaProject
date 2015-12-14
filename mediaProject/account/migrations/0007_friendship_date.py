# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_friendship_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 14, 21, 0, 29, 935198, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
