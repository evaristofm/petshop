from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    PetListView, PetDetailView,
    PetCreateView, PetUpdateView,
    PetDeleteView, CustomLoginView,
    RegisterPage
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', PetListView.as_view(), name="pet-list"),
    path('pet/add/', PetCreateView.as_view(), name='pet-add'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('pet/<int:pk>/update', PetUpdateView.as_view(), name='pet-update'),
    path('pet/<int:pk>/delete', PetDeleteView.as_view(), name='pet-delete'),
    
]
