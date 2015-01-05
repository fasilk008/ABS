# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='docfile',
            field=models.FileField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pages',
            name='desc',
            field=models.CharField(help_text=b'Description for the page', max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pages',
            name='header',
            field=models.CharField(help_text=b'Header for the page', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pages',
            name='type',
            field=models.CharField(help_text=b'Type of the page', max_length=1, choices=[(b'1', b'Home'), (b'2', b'Service'), (b'3', b'About'), (b'4', b'Faq')]),
            preserve_default=True,
        ),
    ]
