# Generated by Django 3.2.8 on 2022-03-15 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_auto_20220315_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='customer',
        ),
    ]