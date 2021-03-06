# Generated by Django 4.0.4 on 2022-06-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_ouser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouser',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AddField(
            model_name='ouser',
            name='address2',
            field=models.CharField(blank=True, default='address2', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouser',
            name='country',
            field=models.CharField(blank=True, default='Country', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouser',
            name='state',
            field=models.CharField(blank=True, default='State', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ouser',
            name='tel',
            field=models.CharField(blank=True, default='Telphone', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouser',
            name='zipcode',
            field=models.CharField(default='Zipcode', max_length=300, null=True),
        ),
    ]
