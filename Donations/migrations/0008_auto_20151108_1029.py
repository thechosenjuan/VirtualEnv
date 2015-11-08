# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0007_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/static/img'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/static/img'), upload_to=b''),
        ),
    ]
