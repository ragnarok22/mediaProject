# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_auto_20151124_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 16, 13, 43, 36, 952908, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
