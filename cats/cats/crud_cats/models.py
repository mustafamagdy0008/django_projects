from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.


class Breed(models.Model):
	name = models.CharField(
			max_length=200,
			help_text='Enter The Bread of the cat (e.g. Balinese)',
			validators=[MinLengthValidator(2, "The Bread must be greater than 1 character")]
			)

	def __str__(self):
		return self.name


class Cat(models.Model):
	nickname = models.CharField(max_length=200)
	weight = models.FloatField()
	food = models.CharField(max_length=300)
	breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nickname

