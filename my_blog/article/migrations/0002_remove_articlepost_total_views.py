# Generated by Django 2.2 on 2024-09-03 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='total_views',
        ),
    ]
