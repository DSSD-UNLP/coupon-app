# Generated by Django 2.1.2 on 2018-10-22 23:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0002_auto_20181015_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='availability',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
