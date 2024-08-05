from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeAutos.as_view(), name='autos'),
    path('make/', views.Make.as_view(), name='make'),
    path('auto/', views.Auto.as_view(), name='auto'),
    path('view-makes/', views.ViewMakes.as_view(), name='view-makes'),
    path('view-make/<int:make_id>/', views.ViewMake.as_view(), name='view-make'),
    path('update-make/<int:make_id>/', views.UpdateMake.as_view(), name='update-make'),
    path('delete-make/<int:make_id>/', views.delete_make, name='delete-make'),
]
