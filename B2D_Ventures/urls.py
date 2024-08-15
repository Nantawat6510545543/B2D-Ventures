from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]