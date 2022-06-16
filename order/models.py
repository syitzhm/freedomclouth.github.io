from django.db import models

# Create your models here.
from django.urls import reverse

from clouth import settings
from customize.models import Category


class Ordermaster(models.Model):
    order_id = models.IntegerField('Order id')
    firstName = models.CharField(max_length=300, default='First Name')
    lastName = models.CharField(max_length=300, default='Last Name')
    email = models.CharField(max_length=300, default='email@email.com')
    tel = models.CharField(max_length=100, default='Telphone')
    ship_to_address = models.CharField(max_length=100, default='address')
    ship_to_address2 = models.CharField(max_length=100, default='address2',null=True,blank=True)
    ship_to_country = models.CharField(max_length=100, default='Country')
    ship_to_state = models.CharField(max_length=50, default='State')
    ship_to_zipcode = models.CharField(max_length=300, default='Zipcode',null=True)
    price = models.CharField(max_length=100,null=True)
    quotation_id = models.IntegerField('询价号')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    sleeve = models.CharField(max_length=50, default='袖子',null=True)
    color = models.CharField(max_length=50, default='颜色',null=True)
    size = models.CharField(max_length=50, default='尺寸',null=True)
    gender = models.CharField(max_length=50, default='性别',null=True)
    part_number = models.CharField(max_length=50, default='物料编码',null=True)
    quantity = models.IntegerField(max_length=50,default=0,null=True)
    req_image = models.ImageField(verbose_name="定制样式图片",null=True)
    description = models.CharField('需求描述', max_length=230, default='需求描述',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_open = models.BooleanField(default=True)
    rep_id = models.BooleanField(settings.AUTH_USER_MODEL,default=False)
    category_name = models.ForeignKey(Category, max_length=20,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = verbose_name
        ordering = ['order_id']

    def __str__(self):
        return str(self.order_id)

    def get_absolute_url(self):
        return reverse('order:ordermaster', args=[self.order_id])

    def get_order_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Ordermaster.objects.filter(order_id=self)

class Cartmaster(models.Model):
    cart_id = models.CharField(max_length=100, default='购物车号码')
    price = models.CharField(max_length=100)
    quotation_id = models.CharField(max_length=100, default='quotation号码')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    sleeve = models.CharField(max_length=50, default='袖子')
    color = models.CharField(max_length=50, default='颜色')
    size = models.CharField(max_length=50, default='尺寸')
    gender = models.CharField(max_length=50, default='性别')
    part_number = models.CharField(max_length=50, default='物料编码')
    quantity = models.CharField(max_length=50,default=0)
    req_image = models.ImageField(verbose_name="定制样式图片")
    description = models.CharField('需求描述', max_length=230, default='需求描述',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_open = models.BooleanField(default=True)
    rep_id = models.CharField(max_length=50, default='业务员')
    category_name = models.ForeignKey(Category, max_length=20,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        ordering = ['cart_id']

    def __str__(self):
        return self.cart_id

    # def get_absolute_url(self):
    #     return reverse('order:cartmaster', args=[self.cart_id])

    def get_order_list(self):
        '''返回当前标签下所有购物车列表'''
        return Cartmaster.objects.filter(cart_id=self)