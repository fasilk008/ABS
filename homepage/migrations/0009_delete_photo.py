# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
