from django.urls import path
from . import views
from .views import main, about, get_user, get_all_users, user_orders, order_full, get_user_Moscow, get_user_Saint_Petersburg, product_form

"""
path('', views.main, name='main'),
path('about/', views.about, name='about'),
"""
urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('get_user/<int:user_id>', get_user, name='get_user'),
    path('get_all_users/', get_all_users, name='get_all_users'),
    path('user_orders/<int:user_id>', user_orders, name='user_orders'),
    path('order_full/', order_full, name='order_full'),
    path('get_user_Moscow/', get_user_Moscow, name='get_user_Moscow'),
    path('get_user_Saint_Petersburg/', get_user_Saint_Petersburg, name='get_user_Saint_Petersburg'),
    path('product_form/', product_form, name='product_form'),
]