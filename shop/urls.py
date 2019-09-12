from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('orders', views.orders, name='orders'),
    path('related_products', views.related_products, name='related_products'),
]
