from django.urls import path
from .views import *
urlpatterns = [
    path('events', EventLogView.as_view()),
    path('create-event', CreateEventView.as_view()),
    path('application-user', ApplicationUserView.as_view()),
    path('create-application-user', CrateApplicationUserView.as_view())
]
