# Generated by Django 3.2.2 on 2022-06-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmaster',
            name='cart_id',
            field=models.CharField(default='购物车号码', max_length=100),
        ),
    ]
