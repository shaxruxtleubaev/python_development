from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'update_date')
	list_display_links = ('title',)
	search_fields = ('title',)
	ordering = ('title',)

admin.site.register(Page, PageAdmin)


