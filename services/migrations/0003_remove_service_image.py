# Generated by Django 5.1.1 on 2024-10-04 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_id_alter_submission_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
