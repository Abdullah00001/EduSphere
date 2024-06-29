# Generated by Django 5.0.6 on 2024-06-29 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_bookmodel_book_quantity'),
        ('review', '0002_rename_book_reviewmodel_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmodel',
            name='review',
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='book.bookmodel'),
        ),
    ]
