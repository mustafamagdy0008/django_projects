from django.shortcuts import render
from django.views import View
from django.views import generic

from gview.models import Cat, Dog, Horse, Car

# Create your views here.

class CatListView(View):
    def get(self, request):
        stuff = Cat.objects.all()
        cntx = { 'cat_list': stuff }
        return render(request, 'gview/cat_list.html', cntx)


class CatDetailView(View):
    def get(self, request, pk_from_url):
        obj = Cat.objects.get(id=pk_from_url)
        cntx = { 'cat': obj }
        return render(request, 'gview/cat_detail.html', cntx)


class DogListView(View):
    model = Dog
    def get(self, request):
        modelname = self.model._meta.varbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)


class DogDetailView(View):
    model = Dog
    def get(self, request):
        modelname = self.model._meta.varbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname : obj }
        return render(request, 'gview/'+modelname+'_detail.html', cntx)


class HorseListView(generic.ListView):
    # extends DogListView
    model = Horse


class SampleListView(View):
    def get(self, sequest):
        modelname = self.model._meta.varbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)


class CarListView(SampleListView):
    # Has the same syntax as HorseListView
    model = Car


class CarDetailView(SampleListView):
    model = Car
