# Generated by Django 5.1.3 on 2024-12-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_events_end_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Events'},
        ),
    ]
