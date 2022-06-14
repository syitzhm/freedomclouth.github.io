import copy
import json
from decimal import Decimal
from django.conf import settings

from django.forms import model_to_dict

from .models import Cartmaster

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        cart = copy.deepcopy(self.cart)
        product_id = str(product.cart_id)
        if product_id not in cart:
            self.cart[product_id] = {'quantity': 0, 'price': product.price}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        cart=copy.deepcopy(self.cart)
        product_ids = cart.keys()
        products = Cartmaster.objects.filter(cart_id__in=product_ids)

        for product in products:
            cart[str(product.cart_id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
