# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_article', '0009_auto_20180202_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frase',
            old_name='body',
            new_name='fr',
        ),
    ]