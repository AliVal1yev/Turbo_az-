# Generated by Django 5.0.6 on 2024-06-14 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_remove_caradvertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='advertisement.caradvertisement'),
        ),
    ]
