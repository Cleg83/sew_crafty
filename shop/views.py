from django.shortcuts import render

from .models import Product

# Create your views here.
def shop_items(request):
    """ Shop view to show all items in the shop """

    shop_items = Product.objects.all()
    # query = None
    # categories = None
    # sort = None
    # direction = None

    # if request.GET:
    #     if 'sort' in request.GET:
    #         sortkey = request.GET['sort']
    #         sort = sortkey
    #         if sortkey == 'name':
    #             sortkey = 'lower_name'
    #             products = products.annotate(lower_name=Lower('name'))
    #         if sortkey == 'category':
    #             sortkey = 'category__name'
    #         if 'direction' in request.GET:
    #             direction = request.GET['direction']
    #             if direction == 'desc':
    #                 sortkey = f'-{sortkey}'
    #         products = products.order_by(sortkey)


    #     if 'category' in request.GET:
    #         categories = request.GET['category'].split(',')
    #         products = products.filter(category__name__in=categories)
    #         categories = Category.objects.filter(name__in=categories)


    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(request, "You didn't enter any search criteria")
    #             return redirect(reverse('products'))
            
    #         queries = Q(name__icontains=query) | Q(description__icontains=query)
    #         products = products.filter(queries)

    # current_sorting = f'{sort}_{direction}'

    context = {
        'shop_items': shop_items,
    }

    return render(request, 'shop/shop.html', context)
