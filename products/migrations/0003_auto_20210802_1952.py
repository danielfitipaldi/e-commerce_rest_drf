# Generated by Django 3.2.4 on 2021-08-02 22:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20210723_2253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalIndicador',
            new_name='HistoricalIndicator',
        ),
        migrations.RenameModel(
            old_name='Indicador',
            new_name='Indicator',
        ),
    ]
