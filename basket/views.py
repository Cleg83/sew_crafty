from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from shop.models import Product

# Create your views here.

def view_basket(request):
    """ A view for the shopping basket """

    template = 'basket/basket.html'
    context = {
        'on_basket_page': True,
    }

    return render(request, template, context)


def add_to_basket(request, item_id):
    """ View to show quantity of each item in shopping basket """

    shop_item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    messages.success(request, f'{shop_item.name} added to basket!')
    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Change the quantity of the specified item in the basket"""

    shop_item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, 'Basket updated')
    else:
        basket.pop(item_id)
        messages.success(request, f'{shop_item.name} removed from your basket')

    request.session['basket'] = basket
    request.session.modified = True
    return redirect(reverse('view_basket'))



def delete_from_basket(request, item_id):
    """Remove selected item from the shopping basket."""
    try:
        shop_item = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        if str(item_id) in basket:
            basket.pop(str(item_id))  
            messages.success(request, f'{shop_item.name} removed from your basket')
        else:
            messages.warning(request, 'The item was not in your basket')

        request.session['basket'] = basket
        request.session.modified = True

        return redirect(reverse('view_basket'))

    except Exception as e:
        error_message = f"Error removing item: {e}"
        messages.error(request, error_message)
        return HttpResponse(error_message, status=500)

