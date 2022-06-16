import copy
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm,save_order_form

# Create your views here.

from django.views import generic

from accounts.models import Ouser
from customize.forms import save_quotation_form
from customize.models import Quotation, Category
from order.models import Cartmaster,Ordermaster


def cartmasterview(request,user_id):
    cart = Cart(request)
    cartmaster= Cartmaster.objects.filter(customer_id=user_id)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {'Cartlist': cartmaster,
               'cart': cart}
    return render(request,'order/cart.html',context)

class checkout(generic.TemplateView):
    template_name = "order/checkout.html"
    
# def addtocart(request):
#     checkedlist = request.POST.getlist('checktocart')
#
#     for i in checkedlist :
#
#         quotation= Quotation.objects.get(quotation_id=i)
#         execstr = Cartmaster.objects.create(cart_id=quotation.quotation_id,
#                                            quotation_id=quotation.quotation_id,
#                                            sleeve=quotation.sleeve,
#                                            color=quotation.color,
#                                            size=quotation.size,
#                                            req_image=quotation.req_image,
#                                            gender=quotation.gender,
#                                            part_number=quotation.part_number,
#                                            quantity=quotation.quantity,
#                                            description=quotation.description,
#                                            category_name=quotation.category_name,
#                                            customer_id=quotation.customer_id,
#                                            rep_id=rep_id)
#         execstr.save()
#     return  render(request,'order/cart.html',context)


def cart_add(request):
    
    checkedlist = request.POST.getlist('checktocart')
    cart=Cart(request)

    # cartmaster = get_object_or_404(Cartmaster, cart_id=checkedlist)
    for cartitem in checkedlist:
        cartmaster = get_object_or_404(Cartmaster, cart_id=cartitem)
        qtyid="qty" + str(cartmaster.quotation_id)
        cartqty=request.POST.get(qtyid)
        cart.add(product=cartmaster, quantity=cartqty, update_quantity=cartqty)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})


    total_price = cart.get_total_price()
    context = {'cartlist': cart,
               'total_price': total_price}
    return render(request,'order/checkout.html',context)

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'order/detail.html', {'cart': cart})


def checkcart(request):
    cart = Cart(request)
    cart.clear()

    # print("======>product_ids",cart.key())
    return render(request,'order/checkout.html')


def SaveToCart(request):
    checkedlist = request.POST.getlist('checktocart')
    # print("ouser_name", type(ouser_name))
    
    for i in checkedlist :
        quotation= Quotation.objects.get(quotation_id=i) 
        # ouser_name=Ouser.objects.get(username=quotation.rep_id)    
        execstr = Cartmaster.objects.create(cart_id=quotation.quotation_id,
                                           quotation_id=quotation.quotation_id,
                                           sleeve=quotation.sleeve,
                                           color=quotation.color,
                                           size=quotation.size,
                                           req_image=quotation.req_image,
                                           gender=quotation.gender,
                                           part_number=quotation.part_number,
                                           quantity=quotation.quantity,
                                           description=quotation.description,
                                           category_name=quotation.category_name,
                                           customer_id=quotation.customer_id,
                                           )
        execstr.save()
        return redirect("order:cartmaster", user_id=request.user.id)


def SaveToOrder(request):
    cart=Cart(request)
    product_ids = cart.keys()
    products = Cartmaster.objects.filter(cart_id__in=product_ids)
    if request.method=="POST":
        save_order = save_order_form(data=request.POST)

        # print("----->debuging  ", request.POST['address'],request.POST['state'],request.POST['zip'],request.POST['firstName'],request.POST['tel'])
        # address=request.POST['ship_to_address']
        # execstr = Ordermaster.objects.create(order_id ="12312312",address=request.POST['ship_to_address'], )                                  
        # execstr.save()
        # return redirect("common:index")
        if save_order.is_valid():
            save_order = save_order.save(commit=False)
            
            for items in cart.cart.keys():
                print("_+_+_+_+_+_items",items['product'])
                    
            # execstr = Ordermaster.objects.create(order_id ="12312312",
            #                                     firstName=request.POST['firstName'],
            #                                     lastName =request.POST['lastName'],
            #                                     email=request.POST['email'],
            #                                     tel = request.POST['tel'],
            #                                     ship_to_address=request.POST['ship_to_address'],
            #                                     ship_to_address2=request.POST['ship_to_address2'],
            #                                     ship_to_country=request.POST['ship_to_country'],
            #                                     ship_to_state=request.POST['ship_to_state'],
            #                                     ship_to_zipcode=request.POST['ship_to_zipcode'],
            #                                     )
            # execstr.save()
            return redirect("common:index")
        else:
            print(save_order.errors)
            return HttpResponse(save_order.errors)

    else:
        save_order = save_order_form()
        context = {'save_order': save_order,
                    }
    return render(request, 'customize/customize.html', context)

def Deletecartitem(request, slug):
    Cartdelitem = Cartmaster.objects.get(cart_id=slug)
    Cartdelitem.delete()
    return redirect("order:cartmaster",user_id=request.user.id)

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Cartmaster, id=product_id)
    cart.remove(product)
    return redirect('order:SaveToCart')