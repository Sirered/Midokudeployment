# Generated by Django 4.2.6 on 2023-10-26 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20231026_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tags',
            new_name='taglist',
        ),
    ]
