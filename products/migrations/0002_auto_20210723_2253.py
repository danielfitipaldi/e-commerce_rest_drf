# Generated by Django 3.2.4 on 2021-07-24 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalproduct',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nome',
            new_name='name',
        ),
    ]
