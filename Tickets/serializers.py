from rest_framework import serializers
from .models import Ticket,Booking
from Hotel.serializers import HotelSerializer
from Flights.serializers import FlightSerializer
class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only =True)
    class Meta:
        model = Ticket
        fields = ("id","owner","email","state","flight","rank","seat")
class BookingSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only =True)
    class Meta:
        model = Booking
        fields = ("id","owner","email","state","hotel","date","days","room")