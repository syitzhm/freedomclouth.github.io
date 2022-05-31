# app名为users下的apps.py



from django.apps import AppConfig


class OauthConfig(AppConfig):
    name = 'accounts'
    verbose_name = '用户管理'
