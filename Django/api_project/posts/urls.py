from django.urls import path
from rest_framework.routers import SimpleRouter
from posts.views import CalendarList, UserList, InviteesList, EventList, UserViewSet
"""
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls
"""

urlpatterns = [
    path('users/', UserList.as_view()),
    path('calendar/', CalendarList.as_view(), name='calendar_list'),
    path('invitees/', InviteesList.as_view(), name='invitees_list'),
    path('event/', EventList.as_view(), name='event_list'),
]