# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20141030_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(help_text=b'Header for the item', max_length=255)),
                ('text', models.CharField(help_text=b'Text for item', max_length=2000)),
                ('image', models.FileField(null=True, upload_to=b'images', blank=True)),
                ('page', models.ForeignKey(to='homepage.Pages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pages',
            name='docfile',
        ),
    ]
