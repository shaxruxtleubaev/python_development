from django.contrib import admin
from accounts.models import CustomUser

from accounts.forms import CustomUserCreationForm
from accounts.forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username', 'name', 'is_staff',]
	list_display_links = ['username',]
	fieldsets = UserAdmin.fieldsets + ((None, {'fields': ("name",)}),)
	add_fieldsets = UserAdmin.fieldsets + (
		(None,
			{
				'fields': ("name",)
				}
			),
		)