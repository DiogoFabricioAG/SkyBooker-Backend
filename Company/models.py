from django.db import models
from django_countries.fields import CountryField
import uuid

class Company(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=40, unique = True)
    banner = models.ImageField(upload_to="companies/", blank=True, null=True)
    country = CountryField()
    
    @property
    def get_url(self):
        if self.banner:
            return "http://127.0.0.1:8000" + self.banner.url 

    @property
    def get_flag(self):
        return "http://127.0.0.1:8000" + self.country.flag
    class Meta:
        verbose_name_plural = "Companies"
