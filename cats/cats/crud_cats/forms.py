from django.forms import ModelForm
from .models import Cat as ModelCat, Breed as ModelBreed


class Breed(ModelForm):
	class Meta:
		model = ModelBreed
		fields = '__all__'

class Cat(ModelForm):
	class Meta:
		model = ModelCat
		fields = '__all__'

