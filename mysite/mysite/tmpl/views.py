from django.shortcuts import render
from django.views import View

# Create your views here.

class GameView(View):
    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, 'tmpl/cond.html', x)


class Simple(View):
    def get(self, request):
        return render(request, 'tmpl/simple.html', {})


class Guess(View):
    def get(self, request, zap):
        context = {'zap': zap}
        return render(request, 'tmpl/guess.html', context=context)
