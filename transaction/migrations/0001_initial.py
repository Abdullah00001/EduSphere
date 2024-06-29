# Generated by Django 5.0.6 on 2024-06-26 10:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(choices=[('Deposite', 'Deposite'), ('Withdraw', 'Withdraw')], max_length=400)),
                ('after_transaction_balance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
