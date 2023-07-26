from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.models import Category, Product


# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Книжный - главная'
    }
    return render(request, 'catalog/index.html', context)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class CategoryProductDetailView(DetailView):
    model = Category
    template_name = 'catalog/product.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_item = self.object
        context['title'] = 'Товары'
        context['object_list'] = category_item.product_set.all()
        return context

class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'category', 'preview_image', 'price', 'specification')
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'category', 'price', 'preview_image', 'specification',)
    success_url = reverse_lazy('catalog:product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
