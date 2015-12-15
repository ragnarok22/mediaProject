# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_friendship_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='sender',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
