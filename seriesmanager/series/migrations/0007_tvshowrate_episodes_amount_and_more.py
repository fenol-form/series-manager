# Generated by Django 4.1.3 on 2022-12-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_tvshowrate_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshowrate',
            name='episodes_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tvshowrate',
            name='viewed_episodes_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]