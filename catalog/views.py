from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Product


# Create your views here.
def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Книжный - главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Книжный - категории'
    }
    return render(request, 'catalog/categories.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Выбранная категория {category_item.name}'
    }
    return render(request, 'catalog/product.html', context)


class ProductListView(ListView):
    model = Product