# Generated by Django 5.0.6 on 2024-06-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imotos/'),
        ),
    ]
