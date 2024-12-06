from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product

# Create your views here.
def shop_items(request):
    """ Shop view to show all items in the shop """

    # Basic view to test that shop items display correctly

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
    }

    return render(request, 'shop/shop.html', context)
