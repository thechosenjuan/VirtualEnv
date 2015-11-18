# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0011_cart_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(to='Donations.Product')),
                ('project', models.ForeignKey(default=1, to='Donations.Project')),
                ('user', models.ForeignKey(to='Donations.User')),
            ],
        ),
    ]
