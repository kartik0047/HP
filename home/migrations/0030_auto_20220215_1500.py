# Generated by Django 3.2.8 on 2022-02-15 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_order_item_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='games',
        ),
        migrations.AddField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.order'),
        ),
    ]
