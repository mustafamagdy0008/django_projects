from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'articles'

urlpatterns = [
    path('', TemplateView.as_view(template_name='articles/home.html'), name='home'),
    path('articles/', views.Posts.as_view(), name='posts'),
    path('article/<int:pk>', views.Post.as_view(), name='post'),
    path('add/article/', views.AddArticle.as_view(), name='add_article'),
    path('update/article/<int:pk>', views.UpdateArticle.as_view(), name='update_article'),
    path('delete/article/<int:pk>', views.DeleteArticle.as_view(), name='delete_article'),
]
