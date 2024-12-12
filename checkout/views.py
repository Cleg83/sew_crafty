from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "There's not currently anything in your basket")
        return redirect(reverse('shop'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public': 'pk_test_51QUs3ADscwJkW4XYHBWj1pMlP8s5oz0sR36I4KXKpg9083GbudywpIbNofJD5OKRl9bJ8dgDDGUvtJnygcMSicrD00iC78KtyX',
        'stripe_secret': 'test stripe secret',
    }

    return render(request, template, context)