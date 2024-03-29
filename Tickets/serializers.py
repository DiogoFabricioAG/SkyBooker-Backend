from rest_framework import serializers
from .models import Ticket
from Flights.serializers import FlightSerializer
class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only =True)
    class Meta:
        model = Ticket
        fields = ("id","owner","email","state","flight","rank","seat")