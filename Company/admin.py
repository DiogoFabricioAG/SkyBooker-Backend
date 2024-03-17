# Importar las bibliotecas necesarias
import uuid
from django.contrib import admin
from django import forms
from django_countries.fields import countries
from .models import Company

# Define un formulario personalizado para el modelo Company
class CompanyAdminForm(forms.ModelForm):
    country = forms.ChoiceField(choices=countries)

    class Meta:
        model = Company
        fields = '__all__'

# Registra el modelo Company con el formulario personalizado
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = ('name', 'country')  # Campos a mostrar en la lista de registros del admin
