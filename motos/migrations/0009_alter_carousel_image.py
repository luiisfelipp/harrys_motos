# Generated by Django 5.0.6 on 2024-06-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0008_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
