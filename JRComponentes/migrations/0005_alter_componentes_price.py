# Generated by Django 5.0.6 on 2024-06-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JRComponentes', '0004_componentes_description_alter_componentes_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentes',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
