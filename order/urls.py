from django.urls import path

from cart.views import OrderCreate

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create')
]
