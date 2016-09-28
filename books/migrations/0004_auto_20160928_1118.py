# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now, help_text='The date the book was added to a shelf', blank=True),
        ),
    ]
