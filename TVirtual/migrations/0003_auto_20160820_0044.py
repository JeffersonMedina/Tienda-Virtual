# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-20 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVirtual', '0002_auto_20160802_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idCA',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='idCA',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ManyToManyField(to='TVirtual.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
