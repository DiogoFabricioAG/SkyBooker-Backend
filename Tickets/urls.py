from django.urls import path
from . import api  
urlpatterns = [
    path("<uuid:id>/",api.get_tickets,name="get_tickets"),
    path("create/<uuid:id>/",api.sell_ticket,name="sell_ticket"),
]