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
from accounts.views import profile_view, change_profile_view
from common import views
from common.views import Index
from accounts.views import dashboard,test,dashboardn,test_json,change_avatar,NotificationView,mark_to_read,mark_to_delete

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(('common.urls', 'common'), namespace='common')),  # blog
    path('accounts/', include('allauth.urls')),  # allauth
    path('profile/', profile_view, name='profile'),
    path('change_avatar/', change_avatar, name='changeavatar'),
    path('accounts/profile/', profile_view, name='profile'),
    path('profile/change/', change_profile_view, name='change_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboardn/', dashboardn, name='dashboardn'),
    path('test1/', test, name='test'),
    path('json/', test_json, name='json_test'),
    path('notification/', NotificationView, name='notification'),
    path('notification/mark-to-read/', mark_to_read, name='mark_to_read'),
    path('notification/mark-to-delete/', mark_to_delete, name='mark_to_delete'),
    # path(r'xadmin/', xadmin.site.urls)
]
