# Generated by Django 3.2.2 on 2022-05-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quotation_id',
            field=models.IntegerField(verbose_name='分类'),
        ),
    ]
