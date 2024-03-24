from django.db import models
from django_countries.fields import CountryField
from Company.models import Company
import uuid




class Flight(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    duration = models.DurationField()
    city = models.CharField(max_length=100)
    fcountry = CountryField()
    tcountry = CountryField()
    seats_t = models.IntegerField()
    seats_v = models.IntegerField()
    company = models.ForeignKey(Company, related_name='flights', on_delete=models.CASCADE)
    departure_date = models.DateTimeField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="flight/")
    @property
    def getCountry(self):
        return self.fcountry.name
    

    @property
    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url 
    @property
    def get_date(self):
        return self.departure_date.strftime("%d/%m/%Y")

    @property
    def get_f_flag(self):
        return "http://127.0.0.1:8000" + self.fcountry.flag
    @property
    def get_t_flag(self):
        return "http://127.0.0.1:8000" + self.tcountry.flag
    def __str__(self) -> str:
        return self.city
class Layover(models.Model):
    country = CountryField()
    flight = models.ForeignKey(Flight, related_name='layovers', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    def __str__(self) -> str:
        return "Escala "+self.country.name
    @property
    def get_flag(self):
        return "http://127.0.0.1:8000" + self.country.flag