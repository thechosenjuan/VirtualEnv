# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0009_auto_20151108_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='productName',
            new_name='product',
        ),
    ]
