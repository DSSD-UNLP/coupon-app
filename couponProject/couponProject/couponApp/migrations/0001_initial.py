# Generated by Django 2.1.1 on 2018-10-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('availability', models.IntegerField()),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
