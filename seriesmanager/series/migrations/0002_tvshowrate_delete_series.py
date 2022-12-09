# Generated by Django 4.1.3 on 2022-12-09 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShowRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('startYear', models.CharField(max_length=10)),
                ('endYear', models.CharField(max_length=10)),
                ('countries', models.CharField(max_length=50)),
                ('genres', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2500)),
                ('isWatching', models.BooleanField(blank=True, null=True)),
                ('isWatched', models.BooleanField(blank=True, null=True)),
                ('userRate', models.IntegerField(blank=True, null=True)),
                ('lastUpdateRate', models.DateTimeField(blank=True, null=True)),
                ('lastUpdateStatus', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Series',
        ),
    ]