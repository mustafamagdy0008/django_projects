from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.forms import ModelForm
from autos.models import MakeModel, AutoModel

class MakeForm(forms.ModelForm):
    class Meta:
        model = MakeModel
        fields = '__all__'



class AutoForm(forms.ModelForm):
    class Meta:
        model = AutoModel
        fields = '__all__'
