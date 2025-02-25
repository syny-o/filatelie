# Generated by Django 5.1 on 2025-01-21 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_address_city_alter_address_country_and_more'),
        ('orders', '0002_order_fk_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fk_profile',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='account.profile'),
        ),
    ]
