from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'gview'

urlpatterns = [
    path('',  TemplateView.as_view(template_name='gview/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='cat'),
    # path('dogs', views.DogListView.as_view(), name='dogs'),
    # path('dog/<int:pk_from_url>', views.DogDetailView.as_view(), name='dog'),
]
