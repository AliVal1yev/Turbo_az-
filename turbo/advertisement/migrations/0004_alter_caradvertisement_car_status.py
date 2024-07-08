# Generated by Django 5.0.6 on 2024-07-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_caradvertisement_car_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caradvertisement',
            name='car_status',
            field=models.CharField(blank=True, choices=[('APPROVE', 'approve'), ('PENDING', 'pending'), ('REJECTED', 'rejected')], default='PENDING', max_length=32, null=True),
        ),
    ]
