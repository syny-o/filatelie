# Generated by Django 5.1 on 2025-01-14 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='Ulice')),
                ('city', models.CharField(max_length=255, verbose_name='Město')),
                ('state', models.CharField(max_length=255, verbose_name='Stát')),
                ('postal_code', models.CharField(max_length=20, verbose_name='PSČ')),
                ('country', models.CharField(max_length=255, verbose_name='Země')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='account.profile')),
            ],
            options={
                'verbose_name': 'Adresa',
                'verbose_name_plural': 'Adresy',
            },
        ),
    ]
