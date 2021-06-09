from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import CreateView

from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import Order, OrderItem


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'order/create.html'
    fields = ['first_name', 'last_name', 'email', 'address']

    def post(self, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm.save
        for item in cart:
            OrderItem.objects.create(
                order=form,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': form})
