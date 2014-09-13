# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('last_edited', models.DateTimeField(verbose_name=b'date edited')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
