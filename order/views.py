from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from django.views import generic

from accounts.models import Ouser
from customize.forms import save_quotation_form
from customize.models import Quotation, Category
from order.models import Cartmaster


def cartmasterview(request,user_id):
    cartmaster= Cartmaster.objects.filter(customer_id=user_id)
    context = {'Cartlist': cartmaster}
    return render(request,'order/cart.html',context)

class checkout(generic.TemplateView):
    template_name = "order/checkout.html"


def SaveToCart(request,slug):
    ouser_name=Ouser.objects.get(id=request.user.id)

    print("ouser_name", type(ouser_name))
    quotationlist = Quotation.objects.filter(quotation_id=slug)
        
    for items in quotationlist:
        execstr = Cartmaster.objects.create(cart_id=items.quotation_id,
                                           quotation_id=items.quotation_id,
                                           sleeve=items.sleeve,
                                           color=items.color,
                                           size=items.size,
                                           req_image=items.req_image,
                                           gender=items.gender,
                                           part_number=items.part_number,
                                           quantity=items.quantity,
                                           description=items.description,
                                           category_name=items.category_name,
                                           customer_id=items.customer_id,
                                           rep_id=ouser_name.username)
        execstr.save()
        return redirect("order:cartmaster", user_id=request.user.id)


def Deletecartitem(request, slug):
    Cartdelitem = Cartmaster.objects.get(cart_id=slug)
    Cartdelitem.delete()
    return redirect("order:cartmaster",user_id=request.user.id)