# Generated by Django 4.1.8 on 2023-04-29 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_remove_attributeeventmodulemapper_attribute_and_more'),
        ('attributes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstractattribute',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='abstractattribute',
            name='type',
        ),
        migrations.DeleteModel(
            name='AttributeDescription',
        ),
        migrations.RemoveField(
            model_name='booleanattribute',
            name='abstractattribute_ptr',
        ),
        migrations.RemoveField(
            model_name='floatattribute',
            name='abstractattribute_ptr',
        ),
        migrations.RemoveField(
            model_name='integerattribute',
            name='abstractattribute_ptr',
        ),
        migrations.RemoveField(
            model_name='stringattribute',
            name='abstractattribute_ptr',
        ),
        migrations.RemoveField(
            model_name='timeattribute',
            name='abstractattribute_ptr',
        ),
        migrations.RemoveField(
            model_name='travelattribute',
            name='abstractattribute_ptr',
        ),
        migrations.DeleteModel(
            name='AbstractAttribute',
        ),
        migrations.DeleteModel(
            name='BooleanAttribute',
        ),
        migrations.DeleteModel(
            name='FloatAttribute',
        ),
        migrations.DeleteModel(
            name='IntegerAttribute',
        ),
        migrations.DeleteModel(
            name='StringAttribute',
        ),
        migrations.DeleteModel(
            name='TimeAttribute',
        ),
        migrations.DeleteModel(
            name='TravelAttribute',
        ),
    ]
