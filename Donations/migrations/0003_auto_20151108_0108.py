# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0002_registration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
