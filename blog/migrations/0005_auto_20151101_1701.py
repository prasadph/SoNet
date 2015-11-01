# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151101_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tagpost',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
