# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0005_person_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(blank=True, upload_to='../media/img/avatars/', verbose_name='Загрузите Ваше главное фото:'),
        ),
    ]
