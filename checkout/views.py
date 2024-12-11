from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
    }

    return render(request, template, context)