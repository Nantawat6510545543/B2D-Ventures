from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import RegisterView, LoginView

from . import views

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('auth/', include('allauth.urls')),

    # Application
    path("", views.index, name="index"),
    path('details/', views.details, name='details'),
    path('accounts/profile/', views.profile, name='profile')
]