"""
Purchase Application URLs Configuration
=======================================

"""

from django.urls import path

from order.views import CartCheckoutView, CartEntityCreateView

app_name = "order"
urlpatterns = [
    path("add-to-cart/", CartEntityCreateView.as_view(), name="add"),
    path("checkout/", CartCheckoutView.as_view(), name="checkout"),
]
