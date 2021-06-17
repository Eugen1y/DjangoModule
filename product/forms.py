from django import forms
from django.forms import ModelForm

from product.models import Product


class ProductCreate(ModelForm):
    model = Product
    fields = ['title', 'amount', 'price', 'description']
