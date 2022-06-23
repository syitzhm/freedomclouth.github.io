# Generated by Django 3.2.2 on 2022-06-21 04:36

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ouser_address_ouser_address2_ouser_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ouser',
            options={'ordering': ['-id'], 'verbose_name': 'User', 'verbose_name_plural': 'User'},
        ),
        migrations.AlterField(
            model_name='ouser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatardefault.png', upload_to=accounts.models.user_directory_path, verbose_name='avatar'),
        ),
    ]