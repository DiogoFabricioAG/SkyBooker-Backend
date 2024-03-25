import django_filters
from .models import Hotel

class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Hotel
        fields = ["name"]