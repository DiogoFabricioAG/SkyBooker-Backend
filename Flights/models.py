from django.db import models
from django_countries.fields import CountryField
from Company.models import Company
import uuid

class Flight(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    duration = models.DurationField()
    fcountry = CountryField()
    tcountry = CountryField()
    company = models.ForeignKey(Company, related_name='flights', on_delete=models.CASCADE)
    departure_date = models.DateTimeField()
    price = models.IntegerField()
    