from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm

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
    
def addtocart(request):
    checkedlist = request.POST.getlist('checktocart')
    
    for i in checkedlist :
        
        quotation= Quotation.objects.get(quotation_id=i) 
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
                                           rep_id=rep_id)
        execstr.save()
    return  render(request,'order/cart.html',context)


def cart_add(request, product_id):
    print("product_id in add",product_id)
    cartmaster= Cartmaster.objects.filter(customer_id=request.user.id)
    context = {'Cartlist': cartmaster}
    cart = Cart(request)  # create a new cart object passing it the request object
    print("cart_add", request) 
    print("=====>cart",cart.session)
    incart = get_object_or_404(Cartmaster, cart_id=product_id) 
    # form = CartAddProductForm(request.POST)
    # print("product_id in add",form.errors)
    # if form.is_valid():
        # cd = form.cleaned_data
    cart.add(product=incart, quantity=10, update_quantity=10)
    print("product_id in add",cart)
    # return redirect('shop:list.html')
    return redirect('order:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'order/detail.html', {'cart': cart})


def checkcart(request):
    cart = Cart(request)
    print("======>cart",Cart.__iter__)
    print("======>cart1",Cart.__len__)
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


def Checkout(request):
    checkedlist = request.POST.getlist('checktoorder')
    # print("ouser_name", type(ouser_name))

    for i in checkedlist:
        quotation = Quotation.objects.get(quotation_id=i)
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

def Deletecartitem(request, slug):
    Cartdelitem = Cartmaster.objects.get(cart_id=slug)
    Cartdelitem.delete()
    return redirect("order:cartmaster",user_id=request.user.id)