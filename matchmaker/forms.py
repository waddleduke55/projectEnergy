from django.db import models
from django.forms import ModelForm
from .models import Seller

# Form for a user to upload a seller to the database.
class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['email', 'phone_number', 'address', 'country_name', 'total_produced_2018_Gwh', 'price_per_kwh']
        labels = {'email':'Email',
                    'phone_number':'Phone Number',
                    'address':'Address',
                    'country_name':'Country',
                    'total_produced_2018_Gwh':'Electricity produced in 2018 (Gwh)',
                    'price_per_kwh':'Price per Kwh'}