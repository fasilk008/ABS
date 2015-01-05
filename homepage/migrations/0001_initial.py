# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=2000)),
                ('type', models.CharField(max_length=1, choices=[(b'1', b'Home'), (b'2', b'Service'), (b'3', b'About'), (b'4', b'Faq')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
