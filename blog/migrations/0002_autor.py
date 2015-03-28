# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
            bases=(models.Model,),
        ),
    ]
