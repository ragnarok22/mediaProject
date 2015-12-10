# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20151124_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='recivied',
            new_name='receiver',
        ),
    ]
