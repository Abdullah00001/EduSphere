# Generated by Django 5.0.6 on 2024-06-26 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_image', models.ImageField(upload_to='book/media/upload')),
                ('book_name', models.CharField(max_length=800)),
                ('book_title', models.CharField(max_length=800)),
                ('book_description', models.TextField()),
                ('book_publisher', models.CharField(max_length=800)),
                ('book_edision', models.CharField(max_length=800)),
                ('number_of_pages', models.IntegerField()),
                ('book_language', models.CharField(max_length=800)),
                ('book_origin', models.CharField(max_length=800)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel')),
            ],
        ),
    ]
