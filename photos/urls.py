from django.urls import path
from . import views
from .views import editPhoto, deletePhoto


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('<int:pk>/edit/', editPhoto.as_view(), name='photo_edit'),
    path('<int:pk>/delete/', deletePhoto.as_view(), name='photo_delete'),
    path('<int:pk>/', views.viewPhoto, name='photo'),
]