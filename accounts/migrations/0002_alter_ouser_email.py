# Generated by Django 3.2.2 on 2022-06-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
