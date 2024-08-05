from django.urls import path, include
from . import views
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('danger/', views.danger),
    path('rest/<int:guess>', views.guessing),
    path('bounce', views.bounce),
    path('', views.home),
    # path('main', TemplateView.as_view(template_name='home/main.html')),
]
