# Generated by Django 3.2.8 on 2021-11-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='qty',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
