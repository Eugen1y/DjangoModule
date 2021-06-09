from django.urls import path

from order.views import OrderCreate
app_name = 'order'
urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create')
]
