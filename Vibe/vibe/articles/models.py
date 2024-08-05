from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


# Create your models here.

class Article(models.Model):
	title = models.CharField(
			max_length=200,
			help_text='Type the title of the article',
			validators=[MinLengthValidator(2, 'title must be more than 1 character')]
		)
	content = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_title(self):
		return self.title

	def get_content(self):
		return self.content

	def get_owner(self):
		return self.owner

	def __str__(self):
		return self.title