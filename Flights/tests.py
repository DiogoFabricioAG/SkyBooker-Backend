from django.test import TestCase
from .models import Flight
from datetime import datetime,timedelta
from Company.models import Company
class FlightTestCase(TestCase):
    def setUp(self) -> None:
        self.company =  Company.objects.create(name="First AirLine MTC.", country="NZ")
        self.flight1 =  Flight.objects.create(duration = timedelta(hours=2), fcountry = "CL",tcountry = "AR",company = self.company,departure_date= datetime(year=2018,month=10,day=1,hour=8),price=1000)
        
        self.flight2 =  Flight.objects.create(duration = timedelta(seconds=7200), fcountry = "CL",tcountry = "PE",company = self.company,
                                              departure_date= datetime(year=2018,month=10,day=6,hour=8),price=1500)

    def test_flight_country(self):
        print(self.flight1.departure_date)
        self.assertEqual(self.flight1.fcountry.name, "Chile")
        self.assertEqual(self.flight2.fcountry.name, "Chile")
        self.assertEqual(self.flight1.tcountry.name, "Argentina")
        self.assertEqual(self.flight2.tcountry.name, "Peru")
    