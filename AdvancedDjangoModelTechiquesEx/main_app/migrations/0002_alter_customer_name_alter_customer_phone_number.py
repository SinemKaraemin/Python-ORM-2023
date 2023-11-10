# Generated by Django 4.2.4 on 2023-11-10 08:10

from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, validators=[main_app.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=13, validators=[main_app.validators.validate_phone_number]),
        ),
    ]