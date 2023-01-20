# Generated by Django 4.1.5 on 2023-01-19 15:05

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, validators=[students.validators.validate_unique_email]),
        ),
    ]