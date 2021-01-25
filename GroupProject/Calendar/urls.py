from django.urls import path
from .views import EventLogView, CreateEventView
urlpatterns = [
    path('events', EventLogView.as_view()),
    path('create-event', CreateEventView.as_view())
]
