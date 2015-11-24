# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_friendship'),
    ]

    u_ = [migrations.AlterField(model_name='userprofile', name='civil_status', field=models.CharField(max_length=1,
                                                                                                      choices=[('M',
                                                                                                                'casado'),
                                                                                                               ('S',
                                                                                                                'soltero'),
                                                                                                               ('F',
                                                                                                                'con novia'),
                                                                                                               ('C',
                                                                                                                'es complicado')],
                                                                                                      default='S'), ),
          migrations.AlterField(model_name='userprofile', name='sex', field=models.CharField(max_length=1, choices=[
              ('M', 'Masculino'), ('W', 'Femenino'), ('U', 'Sin definir')], default='U'), ), ]
    operations = u_
