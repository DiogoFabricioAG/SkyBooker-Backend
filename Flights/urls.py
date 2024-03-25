from django.urls import path
from . import api  
from . import views
urlpatterns = [
    path("",api.get_flights,name="get_companies"),
    path("filters",views.FlightListView.as_view(),name="get_flight_with_filters"),
    path("<uuid:id>",api.get_flight_by_id,name="get_flight_by_id"),
    path("<uuid:id>/layovers",api.get_layover_for_a_flight,name="get_layover_for_a_flight"),
]