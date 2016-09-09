# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.URLField(max_length=500)),
                ('skill_one', models.CharField(max_length=255)),
                ('skill_two', models.CharField(max_length=255)),
                ('skill_three', models.CharField(max_length=255)),
            ],
        ),
    ]
