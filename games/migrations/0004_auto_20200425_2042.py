# Generated by Django 3.0.3 on 2020-04-25 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20200420_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'game', 'verbose_name_plural': 'games'},
        ),
        migrations.AlterModelTable(
            name='review',
            table='games',
        ),
    ]
