from django.urls import path
from . import api  
urlpatterns = [
    path("flight/<uuid:id>/",api.get_tickets,name="get_tickets"),
    path("booking/<uuid:id>/",api.get_booking,name="get_booking"),
    path("booking/create/<uuid:id>/",api.make_booking,name="make_booking"),
    path("flight/create/<uuid:id>/",api.sell_ticket,name="sell_ticket"),
]