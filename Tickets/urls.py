from django.urls import path
from . import api  
urlpatterns = [
    path("flight/<uuid:id>/",api.get_tickets,name="get_tickets"),
    path("booking/<uuid:id>/",api.get_booking,name="get_booking"),
    path("booking/create/<uuid:id>/",api.make_booking,name="make_booking"),
    path("booking/confirm/<str:email>/",api.confirm_reservation,name="confirm_reservation"),
    path("flight/create/<uuid:id>/",api.sell_ticket,name="sell_ticket"),
    path("flight/confirm/<str:email>/",api.confirm_flight,name="confirm_flight"),
    path("flight/cancel/",api.flight_details_by_code_and_email,name="flight_details_by_code_and_email"),
    path("flight/delete/<uuid:id>/",api.delete_tickets_by_id,name="delete_tickets_by_id"),
    path("booking/cancel/",api.booking_details_by_code_and_email,name="booking_details_by_code_and_email"),
    path("booking/delete/<uuid:id>/",api.delete_bookings_by_id,name="delete_bookings_by_id"),
]