# Generated by Django 4.1.8 on 2023-05-04 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_remove_standardeventtemplate_other_optional_modules'),
        ('attributes', '0006_alter_booleanattribute_registration_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AttributeEventModuleMapper',
            new_name='AttributeModule',
        ),
    ]
