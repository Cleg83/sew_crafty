from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'in_stock',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product,  ShopAdmin)
admin.site.register(Category, CategoryAdmin)
