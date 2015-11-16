# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import account.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=account.models.url)),
                ('about_me', models.TextField()),
                ('sign', models.CharField(max_length=100)),
                ('born_date', models.DateField()),
                ('sex', models.CharField(default=b'U', max_length=1, choices=[(b'M', b'Masculino'), (b'W', b'Femenino'), (b'U', b'Sin definir')])),
                ('civil_status', models.CharField(default=b'S', max_length=1, choices=[(b'M', b'casado'), (b'S', b'soltero'), (b'F', b'con novia'), (b'C', b'es complicado')])),
                ('is_conected', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
