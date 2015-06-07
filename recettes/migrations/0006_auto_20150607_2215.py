# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0005_auto_20150607_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='libelle',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
