# custom_admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category
    path('categories/', views.get_all_categories),
    path('categories/add/', views.add_category),
    path('categories/<int:pk>/delete/', views.delete_category),
    # Products
    path('products/', views.get_all_products),
    path('products/add/', views.add_product),
    path('products/<int:pk>/edit/', views.edit_product),
    path('products/<int:pk>/delete/', views.delete_product),
    # Products Images
    path('products/images/add/', views.add_product_image),
    path('products/images/<int:pk>/edit/', views.edit_product_image),
    path('products/images/<int:pk>/delete/', views.delete_product_image),
    # Blogs
    path('blogs/', views.get_all_blogs),
    path('blogs/add/', views.add_blog),
    path('blogs/<int:pk>/delete/', views.delete_blog),

    # Orders
    path('orders/', views.get_all_orders),

    # Quotations
    path('quotations/', views.get_all_quotations),
]
