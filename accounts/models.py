import os
import re
import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from clouth import settings
import markdown

from customize.models import Quotation

emoji_info = [
    [('aini_org', '爱你'), ('baibai_thumb', '拜拜'),
     ('baobao_thumb', '抱抱'), ('beishang_org', '悲伤'),
     ('bingbujiandan_thumb', '并不简单'), ('bishi_org', '鄙视'),
     ('bizui_org', '闭嘴'), ('chanzui_org', '馋嘴')],
    [('chigua_thumb', '吃瓜'), ('chongjing_org', '憧憬'),
     ('dahaqian_org', '哈欠'), ('dalian_org', '打脸'),
     ('ding_org', '顶'), ('doge02_org', 'doge'),
     ('erha_org', '二哈'), ('gui_org', '跪了')],
    [('guzhang_thumb', '鼓掌'), ('haha_thumb', '哈哈'),
     ('heng_thumb', '哼'), ('huaixiao_org', '坏笑'),
     ('huaxin_org', '色'), ('jiyan_org', '挤眼'),
     ('kelian_org', '可怜'), ('kuxiao_org', '允悲')],
    [('ku_org', '酷'), ('leimu_org', '泪'),
     ('miaomiao_thumb', '喵喵'), ('ningwen_org', '疑问'),
     ('nu_thumb', '怒'), ('qian_thumb', '钱'),
     ('sikao_org', '思考'), ('taikaixin_org', '太开心')],
    [('tanshou_org', '摊手'), ('tianping_thumb', '舔屏'),
     ('touxiao_org', '偷笑'), ('tu_org', '吐'),
     ('wabi_thumb', '挖鼻'), ('weiqu_thumb', '委屈'),
     ('wenhao_thumb', '费解'), ('wosuanle_thumb', '酸')],
    [('wu_thumb', '污'), ('xiaoerbuyu_org', '笑而不语'),
     ('xiaoku_thumb', '笑cry'), ('xixi_thumb', '嘻嘻'),
     ('yinxian_org', '阴险'), ('yun_thumb', '晕'),
     ('zhouma_thumb', '怒骂'), ('zhuakuang_org', '抓狂')]
]

def get_emoji_imgs(body):
    '''
    替换掉评论中的标题表情，并且把表情替换成图片地址
    :param body:
    :return:
    '''
    img_url = '<img class="comment-emoji-img" src="/static/comment/weibo/{}.png" title="{}" alt="{}">'
    for i in emoji_info:
        for ii in i:
            emoji_url = img_url.format(ii[0], ii[1], ii[0])
            body = re.sub(':{}:'.format(ii[0]), emoji_url, body)
    tag_info = {
        '<h\d>': '',
        '</h\d>': '<br>',
        '<script.*</script>': '',
        '<meta.*?>': '',
        '<link.*?>': ''
    }
    for k, v in tag_info.items():
        body = re.sub(k, v, body)
    return body


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    timestr = datetime.now().strftime('%Y%m%d/')
    upload_dir = os.path.join('avatar/',timestr,str(instance.id))
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
                                 # processors=[ResizeToFill(80, 80)]
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



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_related',
                               verbose_name='评论人', on_delete=models.CASCADE)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    content = models.TextField('评论内容')
    parent = models.ForeignKey('self', verbose_name='父评论', related_name='%(class)s_child_comments', blank=True,
                               null=True, on_delete=models.CASCADE)
    rep_to = models.ForeignKey('self', verbose_name='回复', related_name='%(class)s_rep_comments',
                               blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        '''这是一个元类，用来继承的'''
        abstract = True



    def content_to_markdown(self):
        to_md = markdown.markdown(self.content,
                                  safe_mode='escape',
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                  ])
        return get_emoji_imgs(to_md)


class ArticleComment(Comment):
    belong = models.ForeignKey(Quotation, related_name='article_comments', verbose_name='所属文章',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['create_date']

class Notification(models.Model):
    create_p = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='提示创建者', related_name='notification_create',
                                 on_delete=models.CASCADE)
    get_p = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='提示接收者', related_name='notification_get',
                              on_delete=models.CASCADE)
    comment = models.ForeignKey(ArticleComment, verbose_name='所属评论', related_name='the_comment',
                                on_delete=models.CASCADE)
    is_read = models.BooleanField('是否已读', default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_related',
                               verbose_name='评论人', on_delete=models.CASCADE)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    content = models.TextField('评论内容')
    parent = models.ForeignKey('self', verbose_name='父评论', related_name='%(class)s_child_comments', blank=True,
                               null=True, on_delete=models.CASCADE)
    rep_to = models.ForeignKey('self', verbose_name='回复', related_name='%(class)s_rep_comments',
                               blank=True, null=True, on_delete=models.CASCADE)

    def mark_to_read(self):
        self.is_read = True
        self.save(update_fields=['is_read'])

    class Meta:
        verbose_name = '提示信息'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return '{}@了{}'.format(self.create_p, self.get_p)