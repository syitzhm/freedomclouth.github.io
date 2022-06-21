import os
import uuid
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    timestr = datetime.now().strftime('%Y/%m/%d/')
    upload_dir = os.path.join('avatar/',timestr)
    # if not os.path.exists(upload_dir): os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def quotation_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    # return the whole path to the file
    return os.path.join(str(instance.quotation_id),filename)

class Ouser(AbstractUser):
    link = models.URLField('个人网址',blank=True,help_text='提示：网址必须填写以http开头的完整形式')
    avatar = ProcessedImageField(upload_to=user_directory_path,
                                 default='avatardefault.png',
                                 verbose_name='avatar',
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
        verbose_name = 'User'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

