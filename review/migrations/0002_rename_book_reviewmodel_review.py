# Generated by Django 5.0.6 on 2024-06-29 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='book',
            new_name='review',
        ),
    ]