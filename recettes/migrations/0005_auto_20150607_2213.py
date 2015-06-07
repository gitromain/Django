# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0004_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='libelle',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
