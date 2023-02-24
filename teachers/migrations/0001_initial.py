# Generated by Django 4.1.7 on 2023-02-24 08:11

import datetime
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(db_column='first name', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(db_column='last name', max_length=50, verbose_name='Last name')),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, validators=[students.validators.ValidateEmailDomain('gmail.com', 'yahoo.com', 'test.com'), students.validators.validate_unique_email])),
                ('salary', models.PositiveIntegerField(default=10000)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
