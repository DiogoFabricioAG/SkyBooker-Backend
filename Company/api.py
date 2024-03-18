from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .models import Company
from .serializers import CompanySerializer
from django.http import JsonResponse

@api_view(["GET"])
@permission_classes([AllowAny])
def get_companies(request,format=None):
    companies = Company.objects.all()
    serializer  = CompanySerializer(companies,many = True)
    return JsonResponse(serializer.data, safe=False) 