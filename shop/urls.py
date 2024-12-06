from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_items, name='shop'),
    path('<int:shop_item_id>/', views.shop_item_info, name='shop_item_info'),
]