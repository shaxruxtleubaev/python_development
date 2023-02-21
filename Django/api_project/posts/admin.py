from django.contrib import admin
from posts.models import Calendar, Event, Invitees

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', )
    list_display_links = ('name', )

admin.site.register(Calendar, CalendarAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startdate', 'enddate', )
    list_display_links = ('name', )

admin.site.register(Event, EventAdmin)

class InviteesAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_id', 'user_id')
    list_display_links = ('id', )

admin.site.register(Invitees, InviteesAdmin)