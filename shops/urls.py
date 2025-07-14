from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('search/', views.search_shops, name='search_shops'),
    path('add/', views.add_shop, name='add_shop'),
    path('pay/<int:shop_id>/', views.make_payment, name='make_payment'),
]
