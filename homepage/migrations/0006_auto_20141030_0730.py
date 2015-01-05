# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20141030_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='type',
            field=models.CharField(help_text=b'Type of the page', unique=True, max_length=7, choices=[(b'Home', b'Home'), (b'Service', b'Service'), (b'About', b'About'), (b'Faq', b'Faq')]),
            preserve_default=True,
        ),
    ]
