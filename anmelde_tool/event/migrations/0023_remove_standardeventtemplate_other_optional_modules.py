# Generated by Django 4.1.8 on 2023-05-04 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_delete_registration_delete_registrationparticipant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardeventtemplate',
            name='other_optional_modules',
        ),
    ]
