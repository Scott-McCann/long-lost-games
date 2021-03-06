# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lostgames', '0003_auto_20160519_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='born',
            field=models.DateField(default='1958-12-8'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lostgames.Game'),
        ),
        migrations.AlterField(
            model_name='review',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lostgames.Game'),
        ),
        migrations.AlterField(
            model_name='review_comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lostgames.Game'),
        ),
    ]
