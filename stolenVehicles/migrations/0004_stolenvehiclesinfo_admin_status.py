# Generated by Django 3.1.6 on 2021-02-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stolenVehicles', '0003_auto_20210220_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='stolenvehiclesinfo',
            name='admin_status',
            field=models.CharField(choices=[('under scrutiny', 'Under Scrutiny'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='under scrutiny', max_length=30),
        ),
    ]
