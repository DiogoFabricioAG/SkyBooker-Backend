import django_filters
from .models import Flight

class FlightFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Flight
        fields = ["city"]