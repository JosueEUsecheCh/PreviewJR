# Generated by Django 5.0.6 on 2024-06-27 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JRAudio_video', '0003_alter_componenteaudiovideo_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componenteaudiovideo',
            old_name='availability',
            new_name='avaiability',
        ),
    ]
