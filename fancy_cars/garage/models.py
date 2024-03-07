from django.db import models
from django.urls import reverse


# Create your models here.
from django.db import models
# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.make}, {self.model}, {self.color}, {self.horsepower}"
    

    def get_absolute_url(self):
        return reverse("car-detail", kwargs={'pk':self.pk})
