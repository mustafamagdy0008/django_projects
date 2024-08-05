from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from autos.forms import MakeForm, AutoForm
from autos.models import MakeModel, AutoModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
class HomeAutos(LoginRequiredMixin, View):
    # get method is for GET request
    def get(self, request):
        return render(request, 'autos/autos.html')


class Make(LoginRequiredMixin, View):
    def get(self, request):
        form = MakeForm()
        ctx = { 'form': form }
        return render(request, 'autos/make-form.html', ctx)

    def post(self, request):
        # print(request.POST)
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
            # reverse is used url name
            return redirect(reverse('make'))
        ctx = {'form': form}
        return render(request, 'autos/make-form.html', ctx)

class Auto(LoginRequiredMixin, View):
    def get(self, request):
        form = AutoForm()
        ctx = { 'form': form }
        return render(request, 'autos/autos-form.html', ctx)

    def post(self, request):
        # print(request.POST)
        # name = request.POST.get('name')
        # make = models.Make(name=name)
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('view-makes'))
        ctx = {'form': form}
        return render(request, 'autos/autos-form.html', ctx)


class ViewMakes(LoginRequiredMixin, View):
    def get(self, request):
        makes = MakeModel.objects.all()
        # print("MAKES", makes)
        ctx = { "makes": makes }
        return render (request, 'autos/view-makes.html', ctx)

class ViewMake(LoginRequiredMixin, View):
    def get(self, request, make_id):
        # print(make_id)
        make = MakeModel.objects.get(id=make_id)
        autos = make.autos.all()
        # print(make)
        # print("MAKE", make)
        ctx = {
            "make": make,
            "autos": autos,
         }
        return render (request, 'autos/view-make.html', ctx)


class UpdateMake(LoginRequiredMixin, View):
    model = MakeModel
    def get(self, request, make_id):
        # print("IAM HERE")
        make = get_object_or_404(self.model, pk=make_id)
        form = MakeForm(instance=make)
        ctx = { 'form': form }
        return render(request, 'autos/make-form.html', ctx)

    def post(self, request, make_id):
        print(request.POST)
        name = request.POST.get('name')
        make = MakeModel.objects.get(id=make_id)
        make.name = name
        make.save()
        print("revers: ", reverse('view-make', args=[make_id]))
        return redirect(reverse('view-make', args=[make_id]))


@login_required
def delete_make(request, make_id):
    make = MakeModel.objects.get(id=make_id)
    if request.method == 'POST':
        make.delete()
        return redirect(reverse('view-makes'))
    return render(request, 'autos/confirm_delete.html', {'auto': make })
