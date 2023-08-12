from django.urls import path
from django.views.decorators.cache import cache_page

from info.apps import InfoConfig
from info.views import InfoCreateView, InfoListView, InfoDetailView, InfoUpdateView, InfoDeleteView

app_name = InfoConfig.name

urlpatterns = [
    path('create/', InfoCreateView.as_view(), name='create'),
    path('info/', cache_page(60)(InfoListView.as_view()), name='list'),
    path('view/<int:pk>/', InfoDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', InfoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', InfoDeleteView.as_view(), name='delete'),
]
