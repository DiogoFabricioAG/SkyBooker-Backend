from rest_framework.decorators import api_view,permission_classes
from Flights.models import Flight
from rest_framework.permissions import AllowAny
from .serializers import TicketSerializer,BookingSerializer
from .models import Ticket,Booking
from Hotel.models import Hotel
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import send_mail
@api_view(["GET"])
@permission_classes([AllowAny])
def get_tickets(request,id,format=None):
    flight = Flight.objects.get(pk = id)
    all_tickets = flight.tickets.all()
    serializer = TicketSerializer(all_tickets,many = True)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["GET"])
@permission_classes([AllowAny])
def get_booking(request,id,format=None):
    hotel = Hotel.objects.get(pk = id)
    all_tickets = hotel.bookings.all()
    serializer = BookingSerializer(all_tickets,many = True)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["POST"])
@permission_classes([AllowAny])
def sell_ticket(request,id,format=None):
    flight= Flight.objects.get(pk = id)
    for seat_code  in request.data['seats']:
        Ticket.objects.create(owner=request.data['name'],flight=flight,email=request.data['email'],seat=seat_code)
    url = f"http://localhost:5173/flight/confirm?email={request.data['email']}"
    # send_mail(
    #     "Confirmación de vuelo",
    #     f"Su vuelo esta casi listo introduzca este link {url} y su compra se habra hecho oficial.",
    #     "skyBooker@official.com",
    #     [request.data['email']],
    #     fail_silently=False,
    # )
    print(f"Correo electrónico a enviar a {request.data['email']}:")
    print(f"Asunto: Confirmación de vuelo")
    print(f"Cuerpo del mensaje: Su vuelo está casi listo. Introduzca este enlace {url} y su compra se habrá hecho oficial.")

    return JsonResponse({"message":"Recibido y creado la orden de pago"})

@api_view(["POST"])
@permission_classes([AllowAny])
def confirm_flight(request,email):
    flight_to_confirm = Ticket.objects.filter(email = email,state = "Inactive").update(state="Active")
    return JsonResponse({"message":"Vuelo confirmado gracias por tu compra 😊"})
    
@api_view(["POST"])
@permission_classes([AllowAny])
def make_booking(request,id,format=None):
    hotel= Hotel.objects.get(pk = id)
    for room_code  in request.data['rooms']:
        Booking.objects.create(owner=request.data['name'],hotel=hotel,days=request.data['days'],date=datetime.strptime(request.data['date'],"%Y-%m-%d").date(),email=request.data['email'],room=room_code)
    return JsonResponse({"message":"Recibido y Creado"})
