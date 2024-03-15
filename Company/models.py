from django.db import models
from django_countries.fields import CountryField
import uuid
class Company(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=40, unique = True)
    banner = models.ImageField(upload_to="companies/", blank=True, null=True)
    country = CountryField()

