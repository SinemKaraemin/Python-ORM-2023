# Generated by Django 4.2.4 on 2023-11-10 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_discount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]
