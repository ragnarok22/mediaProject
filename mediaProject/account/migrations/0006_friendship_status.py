# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20151204_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='status',
            field=models.CharField(default='0', max_length=1, choices=[('0', 'Accepted'), ('1', 'Denied')]),
            preserve_default=False,
        ),
    ]
