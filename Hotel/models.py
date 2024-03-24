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

    @property
    def getCountry(self):
        return self.country.name

    @property
    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url

    @property
    def get_flag(self):
        return "http://127.0.0.1:8000" + self.country.flag
    def __str__(self) -> str:
        return self.name