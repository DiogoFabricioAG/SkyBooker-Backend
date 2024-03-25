from rest_framework.generics import ListAPIView
from .filters import HotelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from .models import Hotel
from .serializers import HotelSerializer


class HotelListView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    permission_classes = [AllowAny]