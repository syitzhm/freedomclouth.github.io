# Generated by Django 3.2.2 on 2022-06-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_cartmaster_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmaster',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
