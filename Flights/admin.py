from django.contrib import admin
from django import forms
from django_countries.fields import countries
from .models import Flight, Layover
class FlightAdminForm(forms.ModelForm):
    fcountry = forms.ChoiceField(choices=countries)
    tcountry = forms.ChoiceField(choices=countries)

    class Meta:
        model = Flight
        fields = '__all__'

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    form = FlightAdminForm
    list_display = ('image','departure_date','duration', 'price','city','fcountry','tcountry','seats_t','seats_v','company')  

class LayoverAdminForm(forms.ModelForm):
    country = forms.ChoiceField(choices=countries)

    class Meta:
        model = Layover
        fields = '__all__'

@admin.register(Layover)
class LayoverAdmin(admin.ModelAdmin):
    form = LayoverAdminForm
    list_display = ("flight","city",'country')  

