from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.list_products, name='products'),
    path('detailed_product/', views.detailed_product, name='detailed_product'),
] 

