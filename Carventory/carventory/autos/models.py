from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class MakeModel(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        return self.name


class AutoModel(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('MakeModel', on_delete=models.CASCADE, related_name='autos',null=False) # If we delete a make the auto will be automatically deleted

    def __str__(self):
        return self.nickname

    def fields(self):
        return [self.nickname, self.mileage, self.comments]
