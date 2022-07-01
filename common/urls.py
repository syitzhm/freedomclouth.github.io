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
from django.urls import path

from common import views
from common.views import Index
app_name="common"


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(('common.urls', 'common'), namespace='common')),  # blog
    path('', views.Index, name='index'),  # Main page
    path('index/', views.Index, name='index'),  # Main page
    path('products/', views.Products.as_view(), name='products'),  # Single product page
    path('single/<slug:slug>', views.Single, name='single'),  # Single product page
    path('mark_to_delete/<slug:slug>/<slug:categoryname>', views.mark_to_delete, name='mark_to_delete'),  # Single product page
    # path(r'xadmin/', xadmin.site.urls)
]
