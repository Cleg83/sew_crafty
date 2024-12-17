from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_orders/<order_number>', views.user_orders, name='user_orders'),
]