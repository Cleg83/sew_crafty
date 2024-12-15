import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from decimal import Decimal

from shop.models import Product
from basket.contexts import basket_contents


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_1 = models.CharField(max_length=80, null=False, blank=False)
    address_2 = models.CharField(max_length=80, null=False, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=20, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    item_count = models.IntegerField(null=False, blank=False, default=0)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    def _create_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = (self.lineitems.aggregate(Sum("item_total"))["item_total__sum"] or 0)
        self.item_count = (self.lineitems.aggregate(Sum("quantity"))["quantity__sum"] or 0 )

        if self.item_count < settings.FREE_DELIVERY_ITEM_THRESHOLD:
            self.delivery_fee = Decimal(settings.STANDARD_DELIVERY_COST)
        else:
            self.delivery_fee = Decimal(0)

        self.grand_total = self.order_total + self.delivery_fee
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class LineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    shop_item = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Set item total and update order total
        """
        self.item_total = self.shop_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.shop_item.sku} on order {self.order.order_number}"
