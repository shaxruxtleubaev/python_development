from posts.models import Calendar, Invitees, Event
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from posts.serializers import UserSerializer, CalendarSerializer, InviteesSerializer, EventSerializer
from posts.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CalendarList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class EventList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class InviteesList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Invitees.objects.all()
    serializer_class = InviteesSerializer