# Generated by Django 5.1.3 on 2024-12-16 18:44

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('default_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('default_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_address_1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_address_2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_town', models.CharField(blank=True, max_length=40, null=True)),
                ('default_county', models.CharField(blank=True, max_length=20, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
