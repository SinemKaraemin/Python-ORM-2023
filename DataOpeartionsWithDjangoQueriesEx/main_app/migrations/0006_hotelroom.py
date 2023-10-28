# Generated by Django 4.2.4 on 2023-10-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField()),
                ('room_Type', models.CharField(choices=[('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Suite', 'Suite')])),
                ('capacity', models.PositiveIntegerField()),
                ('amenities', models.TextField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
