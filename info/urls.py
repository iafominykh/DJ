from django.urls import path

from info.apps import InfoConfig
from info.views import InfoCreateView, InfoListView, InfoDetailView, InfoUpdateView, InfoDeleteView

app_name = InfoConfig.name

urlpatterns = [
    path('create/', InfoCreateView.as_view(), name='create'),
    path('info/', InfoListView.as_view(), name='list'),
    path('view/<int:pk>/', InfoDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', InfoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', InfoDeleteView.as_view(), name='delete'),
]