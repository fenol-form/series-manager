# Generated by Django 4.1.3 on 2022-12-11 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_tvshowrate_isinlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshowrate',
            name='score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
