from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm

# Create your views here.
class Register(View):
	
	submit_model = UserRegisterForm

	def get(self, request):
		form = self.submit_model()
		context = { 'form': form }
		return render(request, 'users/register.html', context)

	def post(self, request):
		form = self.submit_model(request.POST)
		context = { 'form': form }
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f'Account has been created for {username}')
				return redirect('articles:home')
		cleaned_username = form.cleaned_data.get('username')
		messages.success(request, f'Something went wrong with')
		return render(request, 'users/register.html', context)



class Login(LoginView):
	template_name = 'users/login.html'

	def get_redirect_url(self):
		redirect_to = self.request.GET.get('next')
		if redirect_to:
			return redirect_to
		else:
			return super().get_redirect_url()


	def get_success_url(self):
		return reverse_lazy('articles:home')


class Logout(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'users/logout.html')

	def post(self, request):
		logout(request)
		return redirect(reverse('users:login'))


class Profile(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'users/profile.html')