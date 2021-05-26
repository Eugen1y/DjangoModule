from django.contrib import admin
from django.urls import path, include

from product.views import *

urlpatterns = [
    path('product/', ProductsList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/new/', ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/update', ProductUpdate.as_view(), name='product-update')

]
