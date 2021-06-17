'''
This is models of product
'''

from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Category(models.Model):
    '''
    This is Category of products
    '''
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, verbose_name='Описание')

    def __repr__(self):
        return f"<category ('{self.id}')>"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"
        ordering = ['id']
        managed = True  # будет ли создаваться таблица


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=100, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    amount = models.PositiveIntegerField()
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product', verbose_name='Категория')
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Скидка')


    def __repr__(self):
        return f"<product ('{self.id}')>"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.pk})


