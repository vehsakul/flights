from models import *
import django.forms as forms

class AirportForm(forms.ModelForm):
    class Meta():
        model = Airport
        fields = ['city', 'country', 'name']
