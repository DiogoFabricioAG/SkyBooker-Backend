# Importar las bibliotecas necesarias
import uuid
from django.contrib import admin
from django import forms
from django_countries.fields import countries
from .models import Hotel

class HotelAdminForm(forms.ModelForm):
    country = forms.ChoiceField(choices=countries)

    class Meta:
        model = Hotel
        fields = '__all__'

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    list_display = ('name', 'price','city','image','country')  
