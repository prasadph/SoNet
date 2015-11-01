# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_date', models.DateField(default=datetime.datetime(2015, 11, 1, 11, 13, 49, 838204, tzinfo=utc))),
                ('post', models.ForeignKey(to='blog.Post')),
                ('tag', models.ForeignKey(to='blog.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='vote',
            name='_type',
            field=models.CharField(choices=[('U', 'Up vote'), ('D', 'Down vote')], max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', through='blog.TagPost'),
        ),
    ]
