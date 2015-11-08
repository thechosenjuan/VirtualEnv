# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0008_auto_20151108_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.FileField(upload_to=b'img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.FileField(upload_to=b'img'),
        ),
        migrations.AddField(
            model_name='cart',
            name='productName',
            field=models.ForeignKey(to='Donations.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='Donations.User'),
        ),
    ]
