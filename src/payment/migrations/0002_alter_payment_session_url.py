# Generated by Django 5.1.6 on 2025-03-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='session_url',
            field=models.URLField(max_length=500),
        ),
    ]
