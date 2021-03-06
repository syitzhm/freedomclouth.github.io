# Generated by Django 3.2.2 on 2022-05-14 05:18

import customize.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, verbose_name='分类')),
                ('category_id', models.IntegerField(max_length=10)),
                ('part_number', models.CharField(max_length=50, unique=True)),
                ('style', models.ImageField(upload_to=customize.models.category_directory_path)),
                ('description', models.CharField(blank=True, default='类别描述', max_length=230, null=True, verbose_name='类别描述')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_id', models.IntegerField(max_length=20, verbose_name='分类')),
                ('sleeve', models.CharField(default='袖子', max_length=50)),
                ('color', models.CharField(default='颜色', max_length=50)),
                ('size', models.CharField(default='尺寸', max_length=50)),
                ('gender', models.CharField(default='性别', max_length=50)),
                ('part_number', models.CharField(default='物料编码', max_length=50)),
                ('quantity', models.IntegerField(default=0, max_length=10)),
                ('req_image', models.ImageField(upload_to=customize.models.quotation_directory_path, verbose_name='定制样式图片')),
                ('description', models.CharField(default='需求描述', max_length=230, verbose_name='需求描述')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_open', models.BooleanField(default=True)),
                ('is_assinged', models.BooleanField(default=False)),
                ('category_name', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='customize.category')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='客户')),
            ],
            options={
                'verbose_name': '询价',
                'verbose_name_plural': '询价',
                'ordering': ['quotation_id'],
            },
        ),
        migrations.CreateModel(
            name='Quoinprog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_image', models.ImageField(upload_to=customize.models.quotation_directory_path)),
                ('desc_feedback', models.CharField(default='需求描述', max_length=230, verbose_name='需求描述')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('quotation_id', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.PROTECT, to='customize.quotation')),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='业务员')),
            ],
            options={
                'verbose_name': '询价反馈',
                'verbose_name_plural': '询价反馈',
                'ordering': ['quotation_id'],
            },
        ),
    ]
