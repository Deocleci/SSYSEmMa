# Generated by Django 3.2.4 on 2021-06-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employees_birth_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ['name', 'birth_date'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
    ]
