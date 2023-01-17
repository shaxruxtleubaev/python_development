from django.forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):

    required_css_class = 'required'
    class Meta:
        model = Quote
        fields = ('__all__')
