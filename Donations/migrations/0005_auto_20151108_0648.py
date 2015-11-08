# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 6, 48, 3, 55784, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 6, 48, 20, 754115, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
