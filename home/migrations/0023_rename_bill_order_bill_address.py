# Generated by Django 3.2.8 on 2022-02-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_album_movies_musician'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='bill',
            new_name='bill_address',
        ),
    ]
