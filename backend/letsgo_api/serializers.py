from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Event, Outing, Attraction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user= user)
        return user

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields=('id', 'name', 'description', 'location')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'startTime', 'endTime', 'location')

class OutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outing
        fields = ('id', 'name', 'description', 'date', 'owner', 'events')