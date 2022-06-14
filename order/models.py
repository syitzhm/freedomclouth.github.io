from django.db import models

# Create your models here.
from django.urls import reverse

from clouth import settings
from customize.models import Category


class Ordermaster(models.Model):
    order_id = models.IntegerField('询价号')
    ship_to_address = models.CharField(max_length=300, default='发货地址')
    ship_to_city = models.CharField(max_length=100, default='发货城市')
    ship_to_state = models.CharField(max_length=50, default='发货州')
    ship_to_zipcode = models.CharField(max_length=300, default='发货zipcode')
    receiver_name = models.CharField(max_length=100, default='收货人')
    receiver_tel = models.CharField(max_length=100, default='收货人电话')
    price = models.CharField(max_length=100)
    quotation_id = models.IntegerField('询价号')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    sleeve = models.CharField(max_length=50, default='袖子')
    color = models.CharField(max_length=50, default='颜色')
    size = models.CharField(max_length=50, default='尺寸')
    gender = models.CharField(max_length=50, default='性别')
    part_number = models.CharField(max_length=50, default='物料编码')
    quantity = models.IntegerField(max_length=50,default=0)
    req_image = models.ImageField(verbose_name="定制样式图片")
    description = models.CharField('需求描述', max_length=230, default='需求描述',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_open = models.BooleanField(default=True)
    rep_id = models.BooleanField(settings.AUTH_USER_MODEL,default=False)
    category_name = models.ForeignKey(Category, max_length=20,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['order_id']

    def __str__(self):
        return str(self.quotation_id)

    def get_absolute_url(self):
        return reverse('order:cartmaster', args=[self.order_id])

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