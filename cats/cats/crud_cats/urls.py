from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'crud_cats'

urlpatterns = [
	path('', TemplateView.as_view(template_name='crud_cats/home.html'), name='cats_list'),
	path('add/breed', views.AddBreed.as_view(), name='add_breed'),
	path('add/cat', views.AddCat.as_view(), name='add_cat'),
	path('view/breeds', views.ViewBreeds.as_view(), name='view_breeds'),
	path('view/cats', views.ViewCats.as_view(), name='view_cats'),
	path('view/breed/<int:pk>', views.ViewBreed.as_view(), name='view_breed'),
	path('view/cat/<int:pk>', views.ViewCat.as_view(), name='view_cat'),
	path('update/cat/<int:pk>', views.UpdateCat.as_view(), name='update_cat'),
	path('delete/cat/<int:pk>', views.DeleteCat.as_view(), name='delete_cat'),
]