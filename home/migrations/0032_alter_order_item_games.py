# Generated by Django 3.2.8 on 2022-02-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_order_item_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='games',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
