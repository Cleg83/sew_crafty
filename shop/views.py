from django.shortcuts import render

# Create your views here.
def shop_items(request):
    """ Shop view to show all items in the shop """

    return render(request, 'shop/shop.html')