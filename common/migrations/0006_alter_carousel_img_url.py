# Generated by Django 3.2.2 on 2022-05-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_carousel_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='img_url',
            field=models.ImageField(upload_to='carousel/'),
        ),
    ]
