# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160928_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, blank=True, upload_to='cover-photos/'),
        ),
    ]
