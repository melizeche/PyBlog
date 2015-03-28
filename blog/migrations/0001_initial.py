# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Agregado', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
