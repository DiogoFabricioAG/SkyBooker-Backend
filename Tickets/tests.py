from datetime import timedelta, datetime
from django.test import TestCase
from .models import Ticket
from Flights.models import Flight
from Company.models import Company

class TicketsTestCase(TestCase):
    def setUp(self) -> None:
        self.company =  Company.objects.create(name="First AirLine MTC.", country="NZ")
        self.flight1 =  Flight.objects.create(duration = timedelta(hours=2), fcountry = "CL",tcountry = "AR",company = self.company,departure_date= datetime(year=2018,month=10,day=1,hour=8),price=1000)
        
        self.flight2 =  Flight.objects.create(duration = timedelta(seconds=7200), fcountry = "CL",tcountry = "PE",company = self.company,
                                              departure_date= datetime(year=2018,month=10,day=6,hour=8),price=1500)
        self.ticket1 = Ticket.objects.create(owner = "Diogo Fabricio Abregu Gonzales",flight = self.flight1,email="diogofabricio17@gmail.com")
        self.ticket2 = Ticket.objects.create(owner = "Diogo Fabricio Abregu Gonzales",flight = self.flight1,email="diogofabricio17@gmail.com")
        self.ticket3 = Ticket.objects.create(owner = "Diogo Fabricio Abregu Gonzales",flight = self.flight2,email="diogofabricio17@gmail.com")
    def test_tickets_case(self):

        self.assertTrue(self.ticket1.email)