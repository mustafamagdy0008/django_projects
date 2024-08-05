from django.urls import path
from . import views


urlpatterns = [
    path('getform/', views.getform),
    path('postform/', views.postform),
    path('csrfform/', views.csrfform),
    path('guess/', views.ClassView.as_view(), name='classy'),
    path('guess2/', views.AwesomeView.as_view(), name='awesome'),
    path('login/', views.Login.as_view(), name='login'),
]
