# Generated by Django 3.2.2 on 2022-06-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_cartmaster_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmaster',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]