from rest_framework.decorators import api_view,permission_classes
from .models import Flight
from rest_framework.permissions import AllowAny
from .serializers import FlightSerializer, LayoverSerializer
from django.http import JsonResponse

@api_view(["GET"])
@permission_classes([AllowAny])
def get_flights(request,format=None):
    flight = Flight.objects.all()
    serializer  = FlightSerializer(flight,many = True)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["GET"])
@permission_classes([AllowAny])
def get_flight_by_id(request,id,format=None):
    flight = Flight.objects.get(pk=id)
    serializer  = FlightSerializer(flight,)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["GET"])
@permission_classes([AllowAny])
def get_layover_for_a_flight(request,id):
    flight = Flight.objects.get(pk = id)
    layovers = flight.layovers.all()
    serializer = LayoverSerializer(layovers,many = True)
    return JsonResponse({
        "data":serializer.data,
        "get_flag":flight.get_f_flag,
        "country":flight.getCountry
    },safe=False)  