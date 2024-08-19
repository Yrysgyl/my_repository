from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category_list/', views.category, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),  # Создание новой категории
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),  # Детали категории
    path('categories/<slug:slug>/update/', views.update_category, name='update_category'),
    path('categories/<slug:slug>/delete/', views.delete_category, name='delete_category'),

    path('products/', views.product, name='product_list'),  # Список всех продуктов
    path('products/create/', views.create_product, name='create_product'),  # Создание нового продукта
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/<slug:slug>/update/', views.update_product, name='update_product'),
    path('products/<slug:slug>/delete/', views.delete_product, name='delete_product'),
    path('comment/<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
