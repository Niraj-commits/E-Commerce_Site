# Generated by Django 5.1.6 on 2025-02-12 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_comm', '0003_rename_items_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descriptin',
            new_name='description',
        ),
    ]
