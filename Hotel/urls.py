from django.urls import path
from . import api  
from . import views
urlpatterns = [
    path("",api.get_hotels,name="get_hotels"),
    path("filters",views.HotelListView.as_view(),name="get_hotel_with_filters"),
    path("<uuid:id>",api.get_hotel_by_id,name="get_hotel_by_id"),
]