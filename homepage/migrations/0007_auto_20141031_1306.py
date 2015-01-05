# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20141030_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='header',
            field=models.CharField(help_text=b'Header for the item', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
