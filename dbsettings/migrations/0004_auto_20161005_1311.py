# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbsettings', '0003_auto_20160815_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=6000, blank=True),
            preserve_default=True,
        ),
    ]
