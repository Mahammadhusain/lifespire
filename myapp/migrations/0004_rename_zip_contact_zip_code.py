# Generated by Django 4.2.1 on 2023-10-28 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
