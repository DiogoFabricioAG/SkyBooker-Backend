from django.urls import path
from . import api  

urlpatterns = [
    path("",api.get_hotels,name="get_hotels"),
]