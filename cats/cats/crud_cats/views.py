from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from .forms import Breed as BreedForm, Cat as CatForm
from .models import Breed as BreedModel, Cat as CatModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.

def is_db_contains(mdl, obj):
	for instance in mdl.objects.all():
		if instance == obj:
			return True
	return False



class BaseAdd(LoginRequiredMixin, View):
	form_model = None
	model = None
	template_name = ''
	success_url = ''
	def get(self, request):
		form = self.form_model()
		ctx = { 'form': form }
		return render(request, 'crud_cats/'+self.template_name, ctx)
	def post(self, request):
		form = self.form_model(request.POST)
		print(request.POST)
		if form.is_valid and not is_db_contains(self.model, request.POST):
			form.save()
			return redirect(reverse('crud_cats:'+self.success_url))
		ctx = { 'form': form }
		return render(request, 'crud_cats/'+self.template_name, ctx)


class AddBreed(BaseAdd):
	form_model = BreedForm
	model = BreedModel
	template_name = 'add.html'
	success_url = 'cats_list'


# class AddCat(AddBreed):
# 	form_model = CatForm
# 	model = CatModel

class AddCat(OwnerCreateView):
	model = CatModel
	template_name = 'crud_cats/add.html'
	fields = ['nickname', 'weight', 'food', 'breed']

	def get_success_url(self):
		return reverse('crud_cats:cats_list')


class ViewBreeds(LoginRequiredMixin, View):
	model_name = BreedModel
	def get(self, request):
		objs = self.model_name.objects.all()
		ctx = { 'objs': objs }
		return render(request, 'crud_cats/view.html', ctx)


class ViewCats(ViewBreeds):
	model_name = CatModel


# class ViewCats(generic.ListView):
# 	model = CatModel


class ViewBreed(LoginRequiredMixin, View):
	model_name = BreedModel
	template_name = 'view-breed.html'
	def get(self, request, pk):
		obj = get_object_or_404(self.model_name, pk=pk)
		ctx = { 'obj': obj }
		return render(request, 'crud_cats/'+self.template_name, ctx)


class ViewCat(ViewBreed):
	model_name = CatModel
	template_name = 'view-cat.html'



# class UpdateCat(LoginRequiredMixin, View):
# 	model = CatModel
# 	form_model = CatForm
# 	success_url = 'crud_cats:view_cat'
# 	template_name = 'add.html'
# 	def get(self, request, pk):
# 		cat = get_object_or_404(self.model, pk=pk)
# 		form = self.form_model(instance=cat)
# 		ctx = {
# 			'form': form,
# 			'cat': cat,
# 		}
# 		return render(request, 'crud_cats/'+self.template_name, ctx)
# 	def post(self, request, pk):
# 		cat = get_object_or_404(self.model, pk=pk)
# 		form = self.form_model(request.POST, instance=cat)
# 		if form.is_valid():
# 			print('valid')
# 			form.save()
# 			return redirect(reverse(self.success_url, args=[pk]))
# 		ctx = {
# 			'form': form,
# 			'cat': cat,
# 		}
# 		return render(request, 'crud_cats/'+self.template_name, ctx)



class UpdateCat(OwnerUpdateView):
	model = CatModel
	template_name = 'crud_cats/add.html'
	fields = ['nickname', 'weight', 'food', 'breed']

	def get_success_url(self):
		return reverse('crud_cats:cats_list')


# class DeleteCat(UpdateCat):
# 	success_url = 'crud_cats:cats_list'
# 	template_name = 'delete.html'
# 	def post(self, request, pk):
# 		cat = get_object_or_404(self.model, pk=pk)
# 		cat.delete()
# 		return redirect(reverse(self.success_url))


class DeleteCat(OwnerDeleteView):
	model = CatModel
	template_name = 'crud_cats/delete.html'
	success_url = reverse_lazy('crud_cats:cats_list')