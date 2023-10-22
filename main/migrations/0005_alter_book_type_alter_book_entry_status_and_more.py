# Generated by Django 4.2.6 on 2023-10-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_book_type_alter_book_entry_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('Novel', 'Novel'), ('Manga', 'Manga'), ('Manhwa', 'Manhwa'), ('LN', 'Light Novel')], default='Manga', max_length=15),
        ),
        migrations.AlterField(
            model_name='book_entry',
            name='status',
            field=models.CharField(choices=[('D', 'Dropped'), ('F', 'Finished'), ('P', 'Plan to read'), ('O', 'On Hold'), ('R', 'Reading')], default='P', max_length=2),
        ),
        migrations.AlterField(
            model_name='custom_entry',
            name='type',
            field=models.CharField(choices=[('Novel', 'Novel'), ('Manga', 'Manga'), ('Manhwa', 'Manhwa'), ('LN', 'Light Novel')], default='Manga', max_length=15),
        ),
    ]
