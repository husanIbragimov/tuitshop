from django.contrib.auth.models import User
from django.db import models

from apps.base.models import BaseAbstractDate, Variant
from apps.product.models import Product, Color, Size, ProductImage


# Create your models here.


class Cart(BaseAbstractDate):
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)

    @property
    def num_of_items(self):
        cart_items = self.cart_items.all()
        return sum([i.quantity for i in cart_items])

    @property
    def cart_total(self):
        cart_items = self.cart_items.all()
        return sum([i.subtotal for i in cart_items])

    def __str__(self):
        return str(self.session_id)


class Order(BaseAbstractDate):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')

    def __str__(self):
        if self.user:
            return f"{self.user.username}"
        return self.phone_number

    @property
    def num_of_items(self):
        cart_items = self.order_items.all()
        return sum([i.quantity for i in cart_items])

    @property
    def cart_total(self):
        cart_items = self.order_items.all()
        return sum([i.subtotal for i in cart_items])


class CartItem(BaseAbstractDate):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name="cart_items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='variant_cart_items')
    product_image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.subtotal}'

    @property
    def subtotal(self):
        return round(self.quantity * (
                self.product_image.price_uzs + ((self.variant.percent * self.product_image.price_uzs) / 100)), 2)


class Wishlist(BaseAbstractDate):
    session_id = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id
