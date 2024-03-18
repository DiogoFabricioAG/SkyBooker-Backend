from django.urls import path
from . import api  

urlpatterns = [
    path("",api.get_companies,name="get_companies"),
]