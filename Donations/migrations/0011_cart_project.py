# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0010_auto_20151108_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='project',
            field=models.ForeignKey(default=1, to='Donations.Project'),
        ),
    ]
