from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Register(View):
	def get(self, request):
		form = UserRegisterForm()
		ctx = {'form': form}
		return render(request, 'users/register.html', ctx)
	def post(self, request):
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f'Account has been created for {username}')
				return redirect(reverse('home:home'))
		cleaned_username = form.cleaned_data.get('username')
		messages.success(request, f'Something went wrong with {cleaned_username}')
		ctx = {'form': form}
		return render(request, 'users/register.html', ctx)



class Login(LoginView):
	template_name = 'users/login.html'


class Logout(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'users/logout.html')

	def post(self, request):
		logout(request)
		return redirect(reverse('users:login'))


class Profile(LoginRequiredMixin, View):
	def get(self, request):
		return render('users/profile.html')

