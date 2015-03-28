# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(to='blog.Autor', null=True),
            preserve_default=True,
        ),
    ]
