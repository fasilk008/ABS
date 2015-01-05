# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20141030_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='type',
            field=models.CharField(help_text=b'Type of the page', unique=True, max_length=1, choices=[(b'1', b'Home'), (b'2', b'Service'), (b'3', b'About'), (b'4', b'Faq')]),
            preserve_default=True,
        ),
    ]
