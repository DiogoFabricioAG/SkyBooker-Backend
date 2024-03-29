from rest_framework.decorators import api_view,permission_classes
from Flights.models import Flight
from rest_framework.permissions import AllowAny
from .serializers import TicketSerializer
from .models import Ticket
from django.http import JsonResponse

@api_view(["GET"])
@permission_classes([AllowAny])
def get_tickets(request,id,format=None):
    flight = Flight.objects.get(pk = id)
    all_tickets = flight.tickets.all()
    serializer = TicketSerializer(all_tickets,many = True)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["POST"])
@permission_classes([AllowAny])
def sell_ticket(request,id,format=None):
    flight= Flight.objects.get(pk = id)
    for seat_code  in request.data['seats']:
        Ticket.objects.create(owner=request.data['name'],flight=flight,email=request.data['email'],seat=seat_code)
    return JsonResponse({"message":"Recibido y Creado"})