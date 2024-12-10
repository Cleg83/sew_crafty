from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from shop.models import Product

# Create your views here.

def view_basket(request):
    """ A view for the shopping basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ View to show quantity of each item in shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)



def delete_from_basket(request, item_id):
    """Remove selected item from the shopping basket"""
    try:
        shop_item = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id, None)
        messages.success(request, f'{shop_item.name} removed from your basket')

        request.session['basket'] = basket
        return redirect("/basket/")  # Redirect to basket page or another URL

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

