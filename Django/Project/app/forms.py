from django.forms import ModelForm
from .models import Shop


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = (
            'name',
            'body',
            'date',
            'stock',
            'color',
            'author',
        )