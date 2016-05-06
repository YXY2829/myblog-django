# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160506_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]
