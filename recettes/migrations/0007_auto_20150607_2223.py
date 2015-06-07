# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0006_auto_20150607_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='id_recette',
            field=models.ForeignKey(to='recettes.Recette', null=True, blank=True),
            preserve_default=True,
        ),
    ]
