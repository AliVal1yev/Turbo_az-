# Generated by Django 5.0.6 on 2024-05-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0010_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
