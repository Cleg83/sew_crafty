from django.urls import path
from . import views

urlpatterns = [
    path('view_basket/', views.view_basket, name='view_basket')
]
