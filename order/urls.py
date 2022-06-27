"""common URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.contrib.admindocs import views
from django.urls import path, include
# from account.views import dashboard
from order.views import cartmasterview, SaveToCart, Deletecartitem, checkout, checkcart, cart_add, cart_remove, cart_detail,SaveToOrder,SaveToCartNormal
from common import views
from common.views import Index
from accounts.views import dashboard,test,dashboardn

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(('common.urls', 'common'), namespace='common')),  # blog
    # path('cart/<slug:slug>', cartmasterview.as_view(), name='cartmaster'),  # allauth
    path('cart/<slug:user_id>', cartmasterview, name='cartmaster'),  # allauth
    path('SaveToCart/', SaveToCart, name='SaveToCart'),  # allauth
    path('SaveToCartNormal/<slug:slug>', SaveToCartNormal, name='SaveToCartNormal'),  # allauth
    path('SaveToOrder/', SaveToOrder, name='savetoorder'),  # allauth
    path('deletecartitem/<slug:slug>', Deletecartitem, name='deletecartitem'),  # allauth
    path('checkout/', checkout.as_view(), name='checkout'),
    path('checkcart/', checkcart, name='checkcart'),
    path('cartadd/', cart_add, name='cart_add'),
    path('remove/<slug:product_id>', cart_remove, name='cart_remove'),
    path('cart_detail/', cart_detail, name='cart_detail'),

    # path(r'xadmin/', xadmin.site.urls)
]
