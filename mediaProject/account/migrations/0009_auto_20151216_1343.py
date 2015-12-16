# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20151214_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('0', 'Accepted'), ('1', 'Denied'), ('2', 'Pending')], max_length=1),
        ),
    ]
