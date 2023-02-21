from rest_framework import serializers
from posts.models import Calendar, Invitees, Event
from django.contrib.auth import get_user_model

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'user_id', 'name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('calendar_id', 'user_id', 'name', 'location', 'startdate', 'enddate', )

class InviteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitees
        fields = ('event_id', 'user_id',)