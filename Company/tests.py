from django.test import TestCase
from .models import Company
from django_filters import FilterSet, CharFilter

class CompanyFilter(FilterSet):
    country = CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['country']

class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name="First AirLine MTC.", country="NZ")

    def test_country_code(self):
        # Filtrar las empresas por país
        qs = Company.objects.all()
        filtro = CompanyFilter({'country': 'u'}, queryset=qs)
        empresas = filtro.qs

        # Comprobar si alguna empresa está en la lista filtrada
        self.assertEqual(empresas.count(),0)
