import xadmin
from django.contrib import admin
from accounts.models import Ouser


# @admin.register(Ouser)
# class OuserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
#     fieldsets = (
#         ('基础信息', {'fields': (('username', 'email'), ('link',))}),
#         ('权限信息', {'fields': (('is_active', 'is_staff', 'is_superuser'),
#                              'groups', 'user_permissions')}),
#         ('重要日期', {'fields': (('last_login', 'date_joined'),)}),
#     )
#     filter_horizontal = ('groups', 'user_permissions',)
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('username', 'email')
from customize.models import Quotation, Category,Quoinprog
from customize.views import QuoinprogView


class QuotationAdmin(object):
    list_display = ('quotation_id', 'customer_id', 'sleeve', 'color', 'size','gender','part_number','image','description','is_open','is_assinged')


xadmin.site.register(Quotation, QuotationAdmin)

class CustomizeAdmin(object):
    list_display = ('author', 'Requirement', 'categoryid')

# xadmin.site.register(Customize, CustomizeAdmin)

class CategoryAdmin(object):
    list_display = ('category_name', 'category_id', 'part_number','style', 'description')

xadmin.site.register(Category, CategoryAdmin)

class QuoinprogAdmin(object):
    model= Quoinprog
    list_display = ('quotation_id', 'customer_id','part_number','image', 'desc_feedback')

xadmin.site.register(Quoinprog,QuoinprogAdmin)
