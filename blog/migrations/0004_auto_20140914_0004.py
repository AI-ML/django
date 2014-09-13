# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=5000)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paragraph', models.CharField(max_length=1000)),
                ('order', models.IntegerField()),
                ('date_published', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('post', models.ForeignKey(to='blog.BlogPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(to='blog.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='paragraph',
            field=models.ForeignKey(to='blog.Paragraphs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(to='blog.BlogPost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='blog.Users'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='edit_date',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='pub_date',
            new_name='date_published',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='content',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='authors',
            field=models.ManyToManyField(to='blog.Users'),
            preserve_default=True,
        ),
    ]
