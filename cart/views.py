from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from product.models import Product
from .cart import Cart

from .forms import CartAddProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'order/create.html'

    def post(self, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm
        if form.is_valid(self):
            order = form.save(self)
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                cart.clear()
                return render(request, 'order/created.html',
                              {'order': order})









