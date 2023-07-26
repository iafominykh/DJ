from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

# Create your views here.
from info.models import Info


class InfoCreateView(CreateView):
    model = Info
    fields = ('title', 'content', 'publication_feature',)
    success_url = reverse_lazy('info:list')

    def form_valid(self, form):
        if form.is_valid():
            new_stat = form.save()
            new_stat.slug = slugify(new_stat.title)
            new_stat.save()
        return super().form_valid(form)


class InfoUpdateView(UpdateView):
    model = Info
    fields = ('title', 'content', 'publication_feature',)

    def form_valid(self, form):
        if form.is_valid():
            new_stat = form.save()
            new_stat.slug = slugify(new_stat.title)
            new_stat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('info:view', args=[self.kwargs.get('pk')])


class InfoDeleteView(DeleteView):
    model = Info
    success_url = reverse_lazy('info:list')


class InfoListView(ListView):
    model = Info

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_feature=True)
        return queryset


class InfoDetailView(DetailView):
    model = Info

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object
