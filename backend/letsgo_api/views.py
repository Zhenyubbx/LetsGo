from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Event, Outing, Attraction
from .serializers import EventSerializer, OutingSerializer, UserSerializer, AttractionSerializer
from tih_api import API

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    @action(detail=True, methods={'GET'})
    def get_attractions(self, searchType, searchvalues):
        response = API.searchAttraction(searchType, searchvalues)
        return Response(response, status=status.HTTP_200_OK)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    @action(detail=True, methods={'GET'})
    def get_attractions(self, searchType, searchvalues):
        response = API.searchAttraction(searchType, searchvalues)
        return Response(response, status=status.HTTP_200_OK)

class OutingViewSet(viewsets.ModelViewSet):
    queryset = Outing.objects.all()
    serializer_class = OutingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )