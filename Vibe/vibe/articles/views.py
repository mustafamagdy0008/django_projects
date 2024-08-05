from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Article as ArticleModel
from .forms import ArticleForm


# Create your views here.
class Posts(LoginRequiredMixin, View):
	
	def get(self, request):
		qs = ArticleModel.objects.all()
		ctx = {'qs': qs}
		return render(request, 'articles/posts.html', ctx)


class Post(LoginRequiredMixin, View):
	
	def get(self, request, pk):
		article = get_object_or_404(ArticleModel, pk=pk)
		ctx = {'article': article}
		return render(request, 'articles/view_article.html', ctx)



class AddArticle(OwnerCreateView):
	model = ArticleModel
	fields = ['title', 'content']
	form = ArticleForm
	template_name = 'articles/create_article.html'
	success_url = reverse_lazy('articles:posts')


class UpdateArticle(OwnerUpdateView):
	model = ArticleModel
	fields = ['title', 'content']
	template_name = 'articles/create_article.html'
	def get_success_url(self):
		return reverse('articles:posts')


class DeleteArticle(OwnerDeleteView):
	model = ArticleModel
	template_name = 'articles/delete_article.html'
	success_url = reverse_lazy('articles:posts')

