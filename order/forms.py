from django import forms
from .models import Ordermaster


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class save_order_form(forms.ModelForm):
    class Meta:
        model = Ordermaster
        fields = ['firstName','lastName','email','tel','ship_to_address',
                  'ship_to_address2','ship_to_country','ship_to_state',
                  'ship_to_zipcode']
