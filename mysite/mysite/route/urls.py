from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'route'

urlpatterns = [
    path('', TemplateView.as_view(template_name='route/main.html')),
    path('first', views.FirstView.as_view(), name='first-view'),
    path('second', views.FirstView.as_view(), name='second-view'),
]
