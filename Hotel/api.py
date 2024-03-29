from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .models import Hotel
from .serializers import HotelSerializer
from django.http import JsonResponse

@api_view(["GET"])
@permission_classes([AllowAny])
def get_hotels(request,format=None):
    companies = Hotel.objects.all()
    serializer  = HotelSerializer(companies,many = True)
    return JsonResponse(serializer.data, safe=False) 
@api_view(["GET"])
@permission_classes([AllowAny])
def get_hotel_by_id(request,id,format=None):
    companies = Hotel.objects.get(pk = id)
    serializer  = HotelSerializer(companies)
    return JsonResponse(serializer.data, safe=False) 