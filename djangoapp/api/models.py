from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.
class Patient(models.Model):
    mrn = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(100), MaxValueValidator(999)])
    name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f'{self.mrn} - {self.name}'