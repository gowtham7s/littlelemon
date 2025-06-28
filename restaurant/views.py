from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
from django.http import HttpResponse

# def sayHello(request):
#  return HttpResponse('Hello World')

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer