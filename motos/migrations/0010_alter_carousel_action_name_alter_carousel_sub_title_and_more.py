# Generated by Django 5.0.6 on 2024-06-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0009_alter_carousel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='action_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='sub_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
