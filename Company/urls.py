from django.urls import path
from . import api  
from . import views
urlpatterns = [
    path("",api.get_companies,name="get_companies"),
    path("<uuid:id>",api.get_data_from_a_company,name="get_data_from_a_company"),
    path("filters",views.CompanyListView.as_view(),name="get_companies_from_a_list_view"),
    
]