from django import forms
from .models import Ordermaster


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class save_order_form(forms.ModelForm):
    class Meta:
        model = Ordermaster
        fields = ['ship_to_address']
        # fields = ['ship_to_address','ship_to_city','ship_to_state','ship_to_zipcode','receiver_name','receiver_tel']
# order_id
    # ship_to_address
    # ship_to_city
    # ship_to_state
    # ship_to_zipcode
    # receiver_name
    # receiver_tel
    # price
    # quotation_id =
    # customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='客户', on_delete=models.PROTECT)
    # sleeve =
    # color =
    # size =
    # gender =
    # part_number =
    # quantity =
    # req_image =