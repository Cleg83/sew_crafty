from django.contrib import admin
from .models import Order, LineItem

# Register your models here.
class OrderItemAdminInline(admin.TabularInline):
    model = LineItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'item_count',
                       'delivery_fee', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid',)
    
    fields = ('order_number', 'date', 'first_name', 
              'last_name', 'email', 'phone_number', 'country', 
              'postcode', 'town', 'address_1', 
              'address_2', 'county', 'item_count', 
              'delivery_fee', 'order_total', 'grand_total',
              'original_basket', 'stripe_pid',)
    
    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_total', 'delivery_fee',
                    'grand_total',)
    
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)