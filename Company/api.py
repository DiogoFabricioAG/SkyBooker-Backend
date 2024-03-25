from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .models import Company
from Flights.serializers import FlightSerializer
from .serializers import CompanySerializer
from django.http import JsonResponse
from rest_framework.generics import ListAPIView





@api_view(["GET"])
@permission_classes([AllowAny])
def get_companies(request,format="api"):
    companies = Company.objects.all()
    serializer  = CompanySerializer(companies,many = True)
    return JsonResponse(serializer.data, safe=False) 

@api_view(["GET"])
@permission_classes([AllowAny])
def get_data_from_a_company(request,id,format=None):
    company = Company.objects.get(pk=id)
    flights = company.flights.all()
    serializer_company = CompanySerializer(company)
    serializer_flights = FlightSerializer(flights,many = True)
    return JsonResponse({
        "company":serializer_company.data,
        "flights": serializer_flights.data

    }, safe=False) 

