from django.contrib import admin

import xadmin
from common.models import Carousel,mainclouth

from xadmin import views


class BaseSetting(object):

    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""

    site_title = "Freedom administration"  # 设置站点标题
    site_footer = "Powered by Ming Zhou"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠，在左侧，默认的

    # 设置models的全局图标, UserProfile, Sports 为表名


xadmin.site.register(views.CommAdminView, GlobalSettings)

# @admin.register(Carousel)
class CarouselAdmin(object):
    list_display = ('number', 'img_url', 'url')

xadmin.site.register(Carousel, CarouselAdmin)

class MainClouthAdmin(object):
    # IMG_LINK = '/static/blog/img/summary.png'
    list_display = ('product_name', 'description','price', 'orig_price', 'img_link','available_inv', 'is_main', 'image','size', 'create_date','update_date','views','slug')

xadmin.site.register(mainclouth, MainClouthAdmin)
