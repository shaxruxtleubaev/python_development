from django.forms import ModelForm
from .models import Quote
from django.contrib.auth.forms import UserCreationForm

class QuoteForm(ModelForm):

	required_css_class = 'required'
	class Meta:
		model = Quote
		fields = ('__all__')

class QuoteUserRegistrationForm(UserCreationForm):

	error_messages = 'Пароли не совпадают!'