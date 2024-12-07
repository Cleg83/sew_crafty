from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        shop_item = get_object_or_404(Product, pk=item_id)
        total += quantity * shop_item.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'shop_item': shop_item,
        })
        
    if item_count < settings.FREE_DELIVERY_ITEM_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
        free_delivery_prompt = settings.FREE_DELIVERY_ITEM_THRESHOLD - item_count
    else:
        delivery = 0
        free_delivery_prompt = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_prompt': free_delivery_prompt,
        'free_delivery_item_threshold': settings.FREE_DELIVERY_ITEM_THRESHOLD,
        'grand_total': grand_total,
    }

    return context