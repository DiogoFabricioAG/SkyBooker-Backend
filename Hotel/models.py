from django.db import models
from django_countries.fields import CountryField
import uuid





class Hotel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100, unique = True)
    price = models.IntegerField()
    city = models.CharField(max_length = 40, unique = True)
    country =  CountryField()
    image = models.ImageField(upload_to="hotel/")
    def __str__(self) -> str:
        return self.name