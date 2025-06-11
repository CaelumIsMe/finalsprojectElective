from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ensure the home view is mapped to the root URL
    path('products/', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('import/', views.product_import, name='product_import'),
    path('export/', views.product_export, name='product_export'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # New URL pattern for product_detail view
    path('soft-deleted/', views.soft_deleted_products, name='soft_deleted_products'),
]