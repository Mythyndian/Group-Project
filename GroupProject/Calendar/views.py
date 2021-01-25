from django.shortcuts import render
from rest_framework import generics
from .serializers import EventLogSerializer, CreateEventSerializer
from .models import EventLog
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class main:
    pass

# Gets all the events


class EventLogView(generics.ListAPIView):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer


class CreateEventView(APIView):
    serializer_class = CreateEventSerializer

    # def post(self, request, format=None):
    #    pass
    """if self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():"""

    # something going to happen
