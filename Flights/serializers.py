from rest_framework import serializers
from .models import Flight, Layover
from Company.serializers import CompanySerializer
class FlightSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Flight
        fields = ("id","duration","fcountry","price","get_date","city","tcountry","seats_t","seats_v","company","getCountry","get_image","get_f_flag","get_t_flag")
class LayoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layover
        fields = ("id","country","get_flag","city")