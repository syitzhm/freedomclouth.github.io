from decimal import Decimal
from django.conf import settings
from order.models import Cartmaster


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        print("==========>inside session", request.session)
        cart = self.session.get(settings.CART_SESSION_ID)
        print("==========>inside cart", request.session)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        print("==========>inside final cart", cart)

    def add(self, product, quantity=1, update_quantity=False):
        print("=========> inside add", product)
        product_id = str(product.cart_id)
        if product_id not in self.cart:
            print("=========> inside add before", self.cart)
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            print("=========> inside add after ", self.cart)
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
        product_ids = self.cart.keys()
        print("======>inside iter product_ids", product_ids)
        products = Cartmaster.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = 10
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
