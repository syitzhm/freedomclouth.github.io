# Generated by Django 3.2.2 on 2022-05-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Sequence ，less than 5 pics', verbose_name='Number')),
                ('img_url', models.ImageField(upload_to='static/carousel')),
                ('url', models.CharField(default='#', help_text='图片跳转的超链接，默认#表示不跳转', max_length=200, verbose_name='url')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
            ],
            options={
                'verbose_name': 'carousel',
                'verbose_name_plural': 'carousel',
                'ordering': ['number', '-id'],
                'get_latest_by': 'create_date',
            },
        ),
        migrations.CreateModel(
            name='mainclouth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('orig_price', models.IntegerField(default=0, verbose_name='orig_price')),
                ('description', models.TextField(max_length=230, verbose_name='Product Description')),
                ('available_inv', models.IntegerField(default=0, verbose_name='available_inv')),
                ('is_main', models.BooleanField(default=False, verbose_name='Index_show')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('size', models.TextField(max_length=230, verbose_name='Size')),
                ('img_link', models.CharField(default='/static/blog/img/summary.png', max_length=255, verbose_name='图片地址')),
                ('image', models.ImageField(upload_to='static/images/photo/%Y%m%d')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
                'ordering': ['-create_date'],
            },
        ),
    ]
