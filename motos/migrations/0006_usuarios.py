# Generated by Django 5.0.6 on 2024-06-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
