from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from cart.forms import CartAddProductForm
from product.models import Product

http_method_names = ['get', 'post', 'update', 'delete']


class ProductsList(ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    extra_context = {'cart_product_form': CartAddProductForm()}


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/product_create.html'
    fields = ['title', 'category', 'price', 'amount', 'description']


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    fields = ['title', 'category', 'price', 'amount', 'description']
