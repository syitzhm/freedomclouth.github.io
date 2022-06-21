import xadmin
from django.contrib import admin
from accounts.models import Ouser


from customize.models import Quotation, Category,Quoinprog
from customize.views import QuoinprogView


class QuotationAdmin(object):
    list_display = ('quotation_id', 'customer_id', 'sleeve', 'color', 'size','gender','part_number','req_image','description','is_open','is_assigned')


xadmin.site.register(Quotation, QuotationAdmin)

class CustomizeAdmin(object):
    list_display = ('author', 'Requirement', 'categoryid')

# xadmin.site.register(Customize, CustomizeAdmin)

class CategoryAdmin(object):
    list_display = ('category_name', 'category_id', 'part_number','style', 'description')

xadmin.site.register(Category, CategoryAdmin)

class QuoinprogAdmin(object):
    model= Quoinprog
    list_display = ('quotation_id',  'desc_feedback', 'rep_id')

xadmin.site.register(Quoinprog,QuoinprogAdmin)
