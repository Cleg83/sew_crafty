from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product

# Create your views here.
def shop_items(request):
    """ Shop view to show all items in the shop """

    # View to display all shop items and provide search functionality

    shop_items = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
        if not query:
            messages.error(request, 'Please enter some search criteria!')
            return redirect(reverse('shop'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        shop_items = shop_items.filter(queries)

    context = {
        'shop_items': shop_items,
        'search_criteria': query,
        'on_shop_page': True,
    }

    return render(request, 'shop/shop.html', context)


def shop_item_info(request, shop_item_id):
    """ Shop item info view """

    shop_item = get_object_or_404(Product, pk=shop_item_id)

    context = {
        'shop_item': shop_item, 
    }

    return render(request, 'shop/shop_item_info.html', context)
