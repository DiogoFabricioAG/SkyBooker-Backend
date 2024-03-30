from django.db import models
from django.utils import timezone
from django.utils import timesince
from Flights.models import Flight
from Hotel.models import Hotel
import uuid

# ****************************************************************
class ReservationBase(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    owner = models.CharField(max_length=50)
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
    class Meta:
        abstract = True

class Ticket(ReservationBase):
    flight = models.ForeignKey(Flight, related_name='tickets', on_delete=models.CASCADE)
    TOURIST = "Tourist"
    VIP =  "VIP"
    CHOICES_RANK = (
        (TOURIST,"Tourist"),
        (VIP,"VIP")
    )
    rank = models.CharField(choices = CHOICES_RANK, max_length = 10, default = TOURIST)
    seat = models.CharField(max_length=10)
    def __str__(self):
        return "Ticket: "+ self.owner + " ("+self.flight.fcountry.name+" -> "+self.flight.tcountry.name+")"
    
class Booking(ReservationBase):
    hotel = models.ForeignKey(Hotel,related_name = "bookings",on_delete = models.CASCADE)
    date = models.DateField()
    days = models.IntegerField()
    room = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"{self.owner}'s Reservation for {self.hotel.name}" 