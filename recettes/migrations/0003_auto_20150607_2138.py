# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recettes', '0002_auto_20150607_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, default=1),
            preserve_default=True,
        ),
    ]
