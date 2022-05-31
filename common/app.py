# app名为users下的apps.py


from django.apps import AppConfig


class UsersConfig(AppConfig):


    # 设置app图标
    app_icon = 'fa fa-line-chart'
    # app名
    name = 'users'
    verbose_name = u'用户管理'
    # __init__.py
    default_app_config = 'users.apps.UsersConfig'


from xadmin import views


class GlobalSetting(object):
    pass