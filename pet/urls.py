from django.urls import path
from .views import (
    PetListView, PetDetailView,
    PetCreateView, PetUpdateView,
    PetDeleteView )

urlpatterns = [
    path('', PetListView.as_view(), name="pet-list"),
    path('add/', PetCreateView.as_view(), name='pet-add'),
    path('<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('<int:pk>/update', PetUpdateView.as_view(), name='pet-update'),
    path('<int:pk>/delete', PetDeleteView.as_view(), name='pet-delete'),
    
]
