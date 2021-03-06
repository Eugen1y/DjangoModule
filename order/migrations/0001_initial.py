# Generated by Django 3.2.3 on 2021-06-16 12:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_delete_brand'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased', models.BooleanField(default=False, verbose_name='cart purchased flag')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='customer')),
            ],
            options={
                'verbose_name': 'shopping cart',
                'verbose_name_plural': 'shopping carts',
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_at', models.DateTimeField(auto_now_add=True, verbose_name='purchased datetime')),
                ('shipping_address', models.TextField()),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.cart', verbose_name='shopping cart')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='CartEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='cart product quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='order.cart', verbose_name='related cart entity')),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='cart product title')),
            ],
            options={
                'verbose_name': 'cart product entity',
                'verbose_name_plural': 'cart product entities',
                'db_table': 'cart_entity',
            },
        ),
    ]
