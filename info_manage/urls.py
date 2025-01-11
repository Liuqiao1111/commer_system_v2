# -*- coding: utf-8`"]
from . import views
from django.urls import path

app_name = 'info_manage'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item_list/<int:category_id>/', views.item_list, name='item_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_order/', views.add_order, name='add_order'),
    path('my_car/', views.my_car, name='my_car'),
    path('my_order/', views.my_order, name='my_order'),
    path('my_info/', views.my_info, name='my_info'),
    path('category_count/', views.category_count, name='category_count'),
    path('top_up/', views.top_up, name='top_up'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('search/', views.search_items, name='search_items'),
]
