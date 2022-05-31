# -*- coding: utf-8 -*-
from django import forms
from accounts.models import Ouser
from customize.models import Quotation,Quoinprog

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ouser
        fields = ['link','avatar']


class save_quotation_form(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['sleeve','color','gender','description']

class save_quofeedback_form(forms.ModelForm):
    class Meta:
        model = Quoinprog
        fields = ['desc_feedback']
        # fields = ['quotationid','customerid','partnum','image','is_open','is_assinged','reg_id','desc_feedback']





