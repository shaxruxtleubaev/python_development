from django.forms import ModelForm
from .models import Listings

class ListingsForm(ModelForm):
    
    class Meta:
        model = Listings
        fields = (
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'square_footage',
            'adress'
        )