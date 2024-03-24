from django.urls import path
from . import api  

urlpatterns = [
    path("",api.get_flights,name="get_companies"),
    path("<uuid:id>",api.get_flight_by_id,name="get_flight_by_id"),
    path("<uuid:id>/layovers",api.get_layover_for_a_flight,name="get_layover_for_a_flight"),
]