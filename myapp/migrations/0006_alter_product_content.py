# Generated by Django 4.2.6 on 2023-10-28 11:52

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=tinymce_4.fields.TinyMCEModelField(blank=True, null=True),
        ),
    ]
