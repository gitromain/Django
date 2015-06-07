# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recettes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etape',
            name='ordre',
        ),
        migrations.AddField(
            model_name='recette',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etape',
            name='libelle',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
