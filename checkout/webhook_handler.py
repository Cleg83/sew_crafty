from django.http import HttpResponse

from .models import Order, LineItem
from shop.models import Product

import stripe
import json
import time


class WH_Handler:
    """Handles stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles generic events from stripe
        """
        return HttpResponse(content=f'Webhook received: {event("type")}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment_intent.succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town__iexact=shipping_details.address.city,
                    address_1__iexact=shipping_details.address.line1,
                    address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town=shipping_details.address.city,
                    address_1=shipping_details.address.line1,
                    address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    shop_item = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = LineItem(
                            order=order,
                            shop_item=shop_item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = LineItem(
                                order=order,
                                shop_item=shop_item,
                                quantity=quantity,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200,
            )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(content=f'Webhook received: {event("type")}', status=200)
