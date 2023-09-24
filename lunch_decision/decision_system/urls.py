from . import views
from django.urls import path, re_path

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant-list'),
    path('restaurants/<int:id>', views.restaurant_detail, name='restaurant'),
    path('restaurants/menu/', views.menu_list, name='menu-list'),
    path('restaurants/menu/<int:id>/', views.menu_detail, name='menu'),
    re_path('login', views.login, name='login'),
    re_path('signup', views.signup, name='signup'),
]
