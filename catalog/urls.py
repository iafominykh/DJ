from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, categories, category_product, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/catalog/', category_product, name='category_product'),
    path('product/', ProductListView.as_view(), name='product_list'),

]