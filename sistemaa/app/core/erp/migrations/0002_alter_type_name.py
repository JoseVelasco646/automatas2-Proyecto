# Generated by Django 5.0.3 on 2024-03-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
    ]
