from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import index, ProductListView, CategoryListView, ProductDetailView, CategoryProductDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/', cache_page(60)(ProductListView.as_view()), name='product_list'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('<int:pk>/product/', cache_page(60)(CategoryProductDetailView.as_view()), name='category_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_confirm_delete'),

]
