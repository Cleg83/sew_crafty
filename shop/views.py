from django.shortcuts import render

from .models import Product

# Create your views here.
def shop_items(request):
    """ Shop view to show all items in the shop """

    # Basic view to test that shop items display correctly

    shop_items = Product.objects.all()
    context = {
        'shop_items': shop_items,
    }

    return render(request, 'shop/shop.html', context)
