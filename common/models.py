import os
import time, datetime
from datetime import date
import random

from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.shortcuts import reverse
import markdown



class mainclouth(models.Model):
    IMG_LINK = '/static/blog/img/summary.png'
    # title = models.CharField('名称', max_length=200, help_text='注意：地址是以http开头的完整链接格式')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.PROTECT)
    product_name = models.CharField('Product Name', max_length=50)
    price = models.DecimalField('price', default=0,max_digits=5, decimal_places=2)
    orig_price = models.DecimalField('orig_price', default=0,max_digits=5, decimal_places=2)
    description = models.TextField('Product Description', max_length=230)
    # category = models.TextField(verbose_name='文章内容', null=True)
    available_inv = models.IntegerField('available_inv', default=0)
    is_main = models.BooleanField('Index_show', default=False)
    create_date = models.DateTimeField(verbose_name='Create time', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Update time', auto_now=True)
    size = models.TextField('Size', max_length=230)
    # body = models.TextField(verbose_name='文章内容',null=True)
    img_link = models.CharField('图片地址', default=IMG_LINK, max_length=255)
    image = models.ImageField(upload_to='static/images/photo/%Y%m%d')
    views = models.IntegerField('Views', default=0)
    slug = models.SlugField(unique=True)
    # is_top = models.BooleanField('置顶', default=False)


    class Meta:
        verbose_name = 'products'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.image.name

# 幻灯片
class Carousel(models.Model):
    number = models.CharField(max_length=50, verbose_name='Number', help_text='Sequence ，less than 5 pics')
    img_url = models.ImageField(upload_to="carousel/")
    # img_url = models.ImageField(upload_to='photo/%Y%m%d')
    url = models.CharField('url', max_length=200, default='#', help_text='图片跳转的超链接，默认#表示不跳转')
    create_date = models.DateTimeField('Create time', auto_now_add=True)

    class Meta:
        verbose_name = 'carousel'
        verbose_name_plural = verbose_name
        get_latest_by = 'create_date'
        # 编号越小越靠前，添加的时间约晚约靠前
        ordering = ['number', '-id']

    def __str__(self):
        return self.number[:25]