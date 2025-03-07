# Generated by Django 3.1.6 on 2021-02-08 05:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(max_length=500, srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Incidences',
            },
        ),
        migrations.CreateModel(
            name='Maha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=101)),
                ('type', models.CharField(max_length=6)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
