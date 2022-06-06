from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

from django.views import generic

from accounts.models import Ouser
from customize.forms import save_quotation_form
from customize.models import Quotation, Category
from order.models import Cartmaster


def cartmasterview(request, user_id):
    cartmaster = Cartmaster.objects.filter(customer_id=user_id)
    context = {'Cartlist': cartmaster}
    return render(request, 'order/cart.html', context)


class checkout(generic.TemplateView):
    template_name = "order/checkout.html"


def cart_add(request, product_id):
    print("product_id in add", product_id)
    cartmaster = Cartmaster.objects.filter(customer_id=request.user.id)
    context = {'Cartlist': cartmaster}
    cart = Cart(request)  # create a new cart object passing it the request object
    print("cart_add", request)
    print("=====>cart", cart.session)
    incart = get_object_or_404(Cartmaster, cart_id=product_id)
    # form = CartAddProductForm(request.POST)
    # print("product_id in add",form.errors)
    # if form.is_valid():
    # cd = form.cleaned_data
    cart.add(product=incart, quantity=10, update_quantity=10)
    print("product_id in add", cart)
    # return redirect('shop:list.html')
    return redirect('order:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'order/detail.html', {'cart': cart})


def checkcart(request):
    cart = Cart(request)
    print("======>cart", Cart.__iter__)
    print("======>cart1", Cart.__len__)
    # print("======>product_ids",cart.key())
    return render(request, 'order/checkout.html')


def SaveToCart(request, slug):
    ouser_name = Ouser.objects.get(id=request.user.id)

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
    return redirect("order:cartmaster", user_id=request.user.id)