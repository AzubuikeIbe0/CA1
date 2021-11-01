from django.urls import path
from django.conf.urls import url
from . import views
from .views import SignUpView, UserEditView, ProfilePageView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    
]