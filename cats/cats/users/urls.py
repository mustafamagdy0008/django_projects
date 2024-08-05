from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
	path('register/', views.Register.as_view(), name='register'),
	path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
	path('profile/', views.Profile.as_view(), name='profile'),
]