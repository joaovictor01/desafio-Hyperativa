# Generated by Django 3.2.25 on 2024-07-29 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardsbatch',
            name='name',
        ),
    ]
