# Generated by Django 3.2.12 on 2024-04-28 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_remove_client_dni_client_curp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='names',
            new_name='name',
        ),
    ]
