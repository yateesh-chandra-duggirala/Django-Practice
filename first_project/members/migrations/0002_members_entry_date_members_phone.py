# Generated by Django 5.0.1 on 2024-01-07 07:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='entry_Date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
