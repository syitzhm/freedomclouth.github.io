# Generated by Django 3.2.2 on 2022-06-23 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220623_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-create_date'], 'verbose_name': 'notification', 'verbose_name_plural': 'notification'},
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='from_user_id',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='to_user_id',
            new_name='to_user',
        ),
    ]
