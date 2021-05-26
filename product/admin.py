from django.contrib import admin
from product.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'slug', 'price', 'amount', 'description']
    list_display = ['title', 'category', 'slug', 'price', 'amount', 'description']
    prepopulated_fields = {'slug': ['title']}
