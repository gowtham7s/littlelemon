from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']  # ✅ Match with your Menu model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =  '__all__' # ['name', 'no_of_guests', 'booking_date']