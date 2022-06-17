import copy
import json
import random
import time
from decimal import Decimal
from django.conf import settings

from django.forms import model_to_dict

from .models import Quotation



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

class addQuotation(object):
    def __init__(self, request):
        print("_++_+_+_+_+_+:in side Quoation class")
        self.session = request.session
        quotation = self.session.get(settings.QUOTATION_SESSION_ID)
        if not quotation:
            quotation = self.session[settings.QUOTATION_SESSION_ID] = {}
        self.quotation = quotation

    def add(self, category, sleeve,color):
        quotation = copy.deepcopy(self.quotation)
        slugstr=  int(time.time())+random.randint(0, 10000)  
        # product_id = str(product.quotation_id)
        # if product_id not in quotation:
        self.quotation[slugstr] = {'quantity': 0, 'sleeve': sleeve,'color': color}
        # if update_quantity:
            # self.quotation[product_id]['quantity'] = quantity
        # else:
        #     self.quotation[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.QUOTATION_SESSION_ID] = self.quotation
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.quotation:
            del self.quotation[product_id]
            self.save()

    def __iter__(self):
        quotation=copy.deepcopy(self.quotation)

        product_ids = quotation.keys()
        products = quotation.objects.filter(quotation_id__in=product_ids)

        for product in products:
            quotation[str(product.quotation_id)]['product'] = product

        for item in quotation.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            # print("_+_+_+_+_+",quotation.values())
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.quotation.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity']) for item in self.quotation.values())

    def clear(self):
        del self.session[settings.QUOTATION_SESSION_ID]
        self.session.modified = True
