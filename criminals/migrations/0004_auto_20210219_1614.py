# Generated by Django 3.1.6 on 2021-02-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0003_auto_20210219_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalsinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('Other', 'Other')], default='null', max_length=5),
        ),
    ]
