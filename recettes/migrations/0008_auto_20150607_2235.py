# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0007_auto_20150607_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id_recette',
            field=models.ForeignKey(null=True, to='recettes.Recette', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='valeur',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
