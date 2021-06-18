"""
Purchase Application Views
==========================

"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, RedirectView, )

from order.forms import CartEntitiesFormSet, OrderForm
from order.models import Cart, Order


class CartEntityCreateView(LoginRequiredMixin, RedirectView):
    """Product add to a product cart view implementation"""

    http_method_names = ["get", "post", "head", "options", "trace"]

    def get_redirect_url(self, *args, **kwargs):
        """Return a redirect URL"""

        return reverse_lazy("product-list")

    def post(self, request, *args, **kwargs):
        """Handle POST request"""

        product_id = request.POST.get("product_id")

        customer = request.user
        cart, _ = Cart.objects.get_or_create(customer=customer, purchased=False)

        entity, created = cart.entities.get_or_create(product_id=product_id)
        if not created:
            entity.quantity += 1

        entity.save()

        return super(CartEntityCreateView, self).post(request, *args, **kwargs)


class CartCheckoutView(CreateView):
    """Cart checkout view implementation"""

    model = Order
    template_name = "purchase/purchase_form.html"
    form_class = OrderForm

    def get_success_url(self):

        return "/"

    def get_cart(self):
        customer = self.request.user
        cart, _ = Cart.objects.get_or_create(customer=customer, purchased=False)

        return cart

    def get_cart_entities(self):
        customer = self.request.user
        try:
            cart = Cart.objects.get(customer=customer, purchased=False)
            return cart.get_entities()

        except Cart.DoesNotExist:
            cart = Cart.objects.create(customer=customer, purchased=False)
            return cart.get_entities()

    def get_context_data(self, **kwargs):
        context = super(CartCheckoutView, self).get_context_data(**kwargs)

        queryset = self.get_cart_entities()
        cart_entities_formset = CartEntitiesFormSet(queryset=queryset)

        context["formset"] = cart_entities_formset

        return context

    def form_valid(self, form):
        formset = CartEntitiesFormSet(self.request.POST)
        if formset.is_valid():
            formset.save()

        cart = self.get_cart()
        form.instance.cart = cart

        return super(CartCheckoutView, self).form_valid(form)
