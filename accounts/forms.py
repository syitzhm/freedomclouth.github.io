# -*- coding: utf-8 -*-
from django import forms
from django.forms import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from accounts.models import Ouser
from customize.models import Category


class TestModelform(forms.ModelForm):
        class Meta:
                model= Category
                fields = ('category_name','category_id','part_number','style','description')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ouser
        fields = ['link','avatar']


