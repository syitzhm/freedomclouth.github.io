import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import request
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from clouth import settings

# def user_directory_path(instance, filename):
#     timestr = datetime.now().strftime('%Y/%m/%d/')
#     upload_dir = os.path.join('paint/',timestr, str(instance.author))
#     # if not os.path.exists(upload_dir): os.makedirs(upload_dir)
#     return os.path.join(upload_dir, filename)

def quotation_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    # return the whole path to the file
    return os.path.join(str(instance.quotation_id),filename)

def category_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    # return the whole path to the file
    return os.path.join(str(instance.category_name),filename)

# 文章分类
class Category(models.Model):
    category_name = models.CharField(verbose_name='分类', max_length=20)
    category_id = models.IntegerField()
    part_number = models.CharField(max_length=50, unique=True)
    style = models.ImageField(upload_to=category_directory_path)
    description = models.CharField(verbose_name='类别描述', max_length=230, default='类别描述',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

    # def get_absolute_url(self):
    #     return reverse('customize:customize', kwargs={'cateid': self.categoryid})
    #
    # def get_article_list(self):
    #     return Category.objects.filter(categoryid=self)

# class Customize(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.PROTECT)
#     Requirement = models.TextField('需求描述', max_length=230, default='特殊需求')
#     create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
#     views = models.IntegerField('阅览量', default=0)
#     categoryid = models.ForeignKey(Category, verbose_name='详细样式', on_delete=models.PROTECT)
#     # tags = models.ManyToManyField(Tag, verbose_name='标签')
#     # keywords = models.ManyToManyField(Keyword, verbose_name='文章关键词',
#     #                                   help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够')
#     class Meta:
#         verbose_name = '定制信息'
#         verbose_name_plural = verbose_name
#         ordering = ['-create_date']
#
#     def __str__(self):
#         return self.categoryid[:20]
#
#     def get_absolute_url(self):
#         return reverse('customize:customize', kwargs={'slug': self.categoryid})
    #
    # def body_to_markdown(self):
    #     return markdown.markdown(self.body, extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #     ])

    # def update_views(self):
    #     self.views += 1
    #     self.save(update_fields=['views'])


class Quotation(models.Model):
    quotation_id = models.IntegerField('id')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    sleeve = models.CharField(max_length=50, default='袖子')
    color = models.CharField(max_length=50, default='颜色')
    size = models.CharField(max_length=50, default='尺寸')
    gender = models.CharField(max_length=50, default='性别')
    part_number = models.CharField(max_length=50, default='物料编码')
    quantity = models.IntegerField(default=0)
    req_image = models.ImageField(upload_to=quotation_directory_path,verbose_name="定制样式图片",null=True,blank=True)
    description = models.CharField('需求描述', max_length=230, default='需求描述',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_open = models.BooleanField(default=True)
    is_assigned = models.BooleanField(default=False)
    category_name = models.ForeignKey(Category, max_length=20,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '询价'
        verbose_name_plural = verbose_name
        ordering = ['quotation_id']

    def __str__(self):
        return str(self.quotation_id)

    #Json
    def get_data(self):
        return {'quotation_id': self.quotation_id,
                # 'customer_id': self.customer_id,
                'sleeve': self.sleeve,
                'color': self.color,
                'size': self.size,
                'gender': self.gender,
                }

    def get_absolute_url(self):
        return reverse('customize:quotationlist_detail', args=[self.quotation_id])

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Quotation.objects.filter(quotation_id=self)


class tempQuotation(models.Model):
    quotation_id = models.IntegerField('id')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    sleeve = models.CharField(max_length=50, default='袖子')
    color = models.CharField(max_length=50, default='颜色')
    size = models.CharField(max_length=50, default='尺寸')
    gender = models.CharField(max_length=50, default='性别')
    part_number = models.CharField(max_length=50, default='物料编码')
    quantity = models.IntegerField(default=0)
    req_image = models.ImageField(upload_to=quotation_directory_path, verbose_name="定制样式图片", null=True, blank=True)
    description = models.CharField('需求描述', max_length=230, default='需求描述', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_open = models.BooleanField(default=True)
    is_assigned = models.BooleanField(default=False)
    category_name = models.ForeignKey(Category, max_length=20, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'tempquotation'
        verbose_name_plural = verbose_name
        ordering = ['quotation_id']

    def __str__(self):
        return str(self.quotation_id)

    # Json
    def get_data(self):
        return {'quotation_id': self.quotation_id,
                # 'customer_id': self.customer_id,
                'sleeve': self.sleeve,
                'color': self.color,
                'size': self.size,
                'gender': self.gender,
                }

    def get_absolute_url(self):
        return reverse('customize:quotationlist_detail', args=[self.quotation_id])

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Quotation.objects.filter(quotation_id=self)

class Quoinprog(models.Model):
    quotation_id = models.ForeignKey(Quotation,  max_length=20,on_delete=models.PROTECT)
    feedback_image = models.ImageField(upload_to=quotation_directory_path)
    desc_feedback = models.CharField(verbose_name='需求描述', max_length=230, default='需求描述')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    rep_id= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='业务员', on_delete=models.PROTECT)

    class Meta:
        verbose_name = '询价反馈'
        verbose_name_plural = verbose_name
        ordering = ['quotation_id']

    def __str__(self):
        return str(self.quotation_id)