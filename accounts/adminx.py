import xadmin
from django.contrib import admin
from accounts.models import Ouser,Notification


@admin.register(Ouser)
class OuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        ('基础信息', {'fields': (('username', 'email'), ('link',))}),
        ('权限信息', {'fields': (('is_active', 'is_staff', 'is_superuser'),
                             'groups', 'user_permissions')}),
        ('重要日期', {'fields': (('last_login', 'date_joined'),)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')


class NotificationAdmin(object):
    list_display = ('from_user', 'to_user', 'is_read', 'content', 'create_date')
    list_filter = ('from_user', 'to_user', 'is_read')
    search_fields = ('from_user', 'to_user')

xadmin.site.register(Notification, NotificationAdmin)