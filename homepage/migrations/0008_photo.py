# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20141031_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(default=None, null=True, upload_to=b'images1', blank=True)),
                ('filename', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
