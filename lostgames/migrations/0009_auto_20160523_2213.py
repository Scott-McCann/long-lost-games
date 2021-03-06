# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 22:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lostgames', '0008_auto_20160520_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('STEALTH', 'Stealth'), ('FPS', 'First-Person Shooter'), ('PUZZLE', 'Puzzle'), ('SIM', 'Simulator'), ('OPEN_WORLD', 'Open World'), ('RPG', 'Role-Playing Game'), ('JRPG', 'Japanese Role-Playing Game'), ('STRATEGY', 'Strategy'), ('MMO', 'Massively Mutliplayer OnLine'), ('PLATFORM', 'Platform'), ('MOBA', 'Mutliplayer Online Battle Arena')], default='Adventure', max_length=128),
        ),
        migrations.AddField(
            model_name='game',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2016, 5, 23)),
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
    ]
