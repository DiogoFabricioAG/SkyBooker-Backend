from django.db import models
from django.utils import timezone
from django.utils import timesince
from Flights.models import Flight
import uuid

class Ticket(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    owner = models.CharField(max_length=50)
    flight = models.ForeignKey(Flight, related_name='tickets', on_delete=models.CASCADE)
    email = models.EmailField()

    ACTIVE = "Active"
    USED = "Used"
    INACTIVE = "Inactive"
    CHOICES_STATE = (
        (ACTIVE,"Active"),
        (USED,"Used"),
        (INACTIVE,"Inactive"),
    )
    state = models.CharField(choices = CHOICES_STATE, max_length = 15, default = ACTIVE)


    def __str__(self):
        return "Ticket: "+self.owner + "("+self.flight.fcountry.name+" -> "+self.flight.tcountry.name+")"