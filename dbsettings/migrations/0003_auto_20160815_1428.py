# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbsettings', '0002_auto_20150703_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
