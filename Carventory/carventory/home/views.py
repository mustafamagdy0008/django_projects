from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home( View):
    def get(self, request):
        return render(request, 'home/main.html', {})
