from rest_framework.decorators import api_view,permission_classes
from Flights.models import Flight
from rest_framework.permissions import AllowAny
from .serializers import TicketSerializer,BookingSerializer
from .models import Ticket,Booking
from Hotel.models import Hotel
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import send_mail
from random import randint
@api_view(["GET"])
@permission_classes([AllowAny])
def get_tickets(request,id,format=None):
    flight = Flight.objects.get(pk = id)
    all_tickets_active = flight.tickets.filter(state="Active")
    all_tickets_inactive = flight.tickets.filter(state="Inactive")
    serializer_active = TicketSerializer(all_tickets_active,many = True)
    serializer_inactive = TicketSerializer(all_tickets_inactive,many = True)

    return JsonResponse({
        "active":serializer_active.data,
        "inactive":serializer_inactive.data,
    }, safe=False) 

@api_view(["GET"])
@permission_classes([AllowAny])
def get_booking(request,id,format=None):
    hotel = Hotel.objects.get(pk = id)
    all_tickets_active = hotel.bookings.filter(state="Active")
    serializer_active = BookingSerializer(all_tickets_active,many = True)
    all_tickets_inactive = hotel.bookings.filter(state="Inactive")
    serializer_inactive = BookingSerializer(all_tickets_inactive,many = True)
    return JsonResponse({
        "active":serializer_active.data,
        "inactive":serializer_inactive.data,
    }, safe=False)

@api_view(["POST"])
@permission_classes([AllowAny])
def sell_ticket(request,id,format=None):
    flight= Flight.objects.get(pk = id)
    code = f"{randint(0,9)}-{randint(0,9)}-{randint(0,9)}-{randint(0,9)}"

    for seat_code  in request.data['seats']:
        Ticket.objects.create(owner=request.data['name'],flight=flight,email=request.data['email'],seat=seat_code,code=code)
    url = f"http://localhost:5173/confirm?email={request.data['email']}&hotel=false&flight=true"
    # send_mail(
    #     "Confirmación de vuelo",
    #     f"Su vuelo esta casi listo introduzca este link {url} y su compra se habra hecho oficial.",
    #     "skyBooker@official.com",
    #     [request.data['email']],
    #     fail_silently=False,
    # )
    print(f"Correo electrónico a enviar a {request.data['email']}:")
    print(f"Asunto: Confirmación de vuelo")
    print(f"Cuerpo del mensaje: Su vuelo está casi listo. Introduzca este enlace {url} y su compra se habrá hecho oficial.\nCodigo: {code}")

    return JsonResponse({"message":"Recibido y creado la orden de pago"})

@api_view(["POST"])
@permission_classes([AllowAny])
def confirm_flight(request,email):
    flight_to_confirm = Ticket.objects.filter(email = email,state = "Inactive").update(state="Active")
    return JsonResponse({"message":"Vuelo confirmado gracias por tu compra 😊"})
    
@api_view(["POST"])
@permission_classes([AllowAny])
def confirm_reservation(request,email):
    hotel_to_confirm = Booking.objects.filter(email = email,state = "Inactive").update(state="Active")
    return JsonResponse({"message":"Reservacion confirmada, disfrute su estadia 😊"})
    
@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_tickets_by_id(request,id):
    ticket = Ticket.objects.get(pk = id)
    ticket.delete()
    return JsonResponse({"message":"Eliminado"})

@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_bookings_by_id(request,id):
    booking = Booking.objects.get(pk = id)
    booking.delete()
    return JsonResponse({"message":"Eliminado"})


@api_view(["POST"])
@permission_classes([AllowAny])
def booking_details_by_code_and_email(request):
    code=request.data['code']
    email = request.data['email']
    Booking_inactive = Booking.objects.filter(state = "Inactive",email=email,code=code)
    serializer = BookingSerializer(Booking_inactive,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(["POST"])
@permission_classes([AllowAny])
def flight_details_by_code_and_email(request):
    code=request.data['code']
    email = request.data['email']
    ticket_inactive = Ticket.objects.filter(state = "Inactive",email=email,code=code)
    serializer = TicketSerializer(ticket_inactive,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(["POST"])
@permission_classes([AllowAny])
def make_booking(request,id,format=None):
    hotel= Hotel.objects.get(pk = id)
    code = f"{randint(0,9)}-{randint(0,9)}-{randint(0,9)}-{randint(0,9)}"

    for room_code  in request.data['rooms']:
        Booking.objects.create(owner=request.data['name'],code=code,hotel=hotel,days=request.data['days'],date=datetime.strptime(request.data['date'],"%Y-%m-%d").date(),email=request.data['email'],room=room_code)
    url = f"http://localhost:5173/confirm?email={request.data['email']}&hotel=true&flight=false"
    # send_mail(
    #     "Confirmación de vuelo",
    #     f"Su vuelo esta casi listo introduzca este link {url} y su compra se habra hecho oficial.",
    #     "skyBooker@official.com",
    #     [request.data['email']],
    #     fail_silently=False,
    # )
    print(f"Correo electrónico a enviar a {request.data['email']}:")
    print(f"Asunto: Confirmación de registro de Hotel")
    print(f"Cuerpo del mensaje: Su vuelo está casi listo. Introduzca este enlace {url} y su compra se habrá hecho oficial.\n Codigo: {code}")
    return JsonResponse({"message":"Recibido y apartado su habitacion, necesita confirmar su compra en su correo"})
