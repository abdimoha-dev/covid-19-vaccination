# Generated by Django 3.1.7 on 2021-03-06 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_registry', '0006_person_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo',
        ),
    ]
