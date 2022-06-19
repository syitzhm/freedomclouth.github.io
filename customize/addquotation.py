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

        self.session = request.session
        newquotation = self.session.get(settings.QUOTATION_SESSION_ID)

        if not newquotation:
            newquotation = self.session[settings.QUOTATION_SESSION_ID] = {}
        self.newquotation = newquotation

    def add(self, category, sleeve,color,size,gender,imagelist,quantity,images,description):
        newquotation = copy.deepcopy(self.newquotation)
        slugstr=  int(time.time())+random.randint(0, 10000)  
        # product_id = str(product.quotation_id)
        # if product_id not in quotation:
        self.newquotation[slugstr] = {'id': slugstr, 'sleeve': sleeve,'size': size,'color': color,'gender': gender,'imagelist': imagelist
                                      ,'quantity': quantity,'images': images,'description': description}

        # if update_quantity:
            # self.quotation[product_id]['quantity'] = quantity
        # else:
        #     self.quotation[product_id]['quantity'] += quantity
        self.save()
        print("_++_+_+_+_+_+:in side Quoations success", newquotation.values())

    def save(self):
        self.session[settings.QUOTATION_SESSION_ID] = self.newquotation
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.newquotation:
            del self.newquotation[product_id]
            self.save()

    # def __iter__(self):
    #     newquotation=copy.deepcopy(self.newquotation)
    #
    #     product_ids = newquotation.keys()
    #     newquotation = Quotation.objects.filter(quotation_id__in=product_ids)
    #
    #     for product in products:
    #         quotation[str(product.quotation_id)]['product'] = product
    #
    #     for item in quotation.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price'] * int(item['quantity'])
    #         # print("_+_+_+_+_+",quotation.values())
    #         yield item

    # def __len__(self):
    #     return sum(int(item['quantity']) for item in self.newquotation.values())
    #
    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * int(item['quantity']) for item in self.newquotation.values())

    def clear(self):
        del self.session[settings.QUOTATION_SESSION_ID]
        self.session.modified = True
