# Generated by Django 4.1.7 on 2023-03-15 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='team',
            new_name='Teams',
        ),
    ]