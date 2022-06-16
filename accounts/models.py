from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Ouser(AbstractUser):
    link = models.URLField('个人网址',blank=True,help_text='提示：网址必须填写以http开头的完整形式')
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )
    email = models.EmailField('email address')
    tel = models.CharField(max_length=100, default='Telphone',null=True,blank=True)
    address = models.CharField(max_length=100, default='address')
    address2 = models.CharField(max_length=100, default='address2',null=True,blank=True)
    country = models.CharField(max_length=100, default='Country',null=True,blank=True)
    state = models.CharField(max_length=50, default='State',null=True,blank=True)
    zipcode = models.CharField(max_length=300, default='Zipcode',null=True)
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

