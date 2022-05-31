# Generated by Django 3.2.2 on 2022-05-16 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0005_rename_is_assinged_quotation_is_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoinprog',
            name='quotation_id',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.PROTECT, related_name='quotation_name', to='customize.quotation'),
        ),
    ]