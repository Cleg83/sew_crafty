from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from.forms import ProfileForm

# Create your views here.
def user_profile(request):
    """A view to show the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your address has been updated.')

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profile/user_profile.html'
    context={
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


def user_orders(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'user_profile/user_orders.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
