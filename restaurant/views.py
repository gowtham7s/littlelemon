from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from .models import Menu, Booking, MenuItem
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from django.http import HttpResponse

@api_view()
@permission_classes([IsAuthenticated])

def securedview(request):
    return HttpResponse('This is a secured view, only accessible to authenticated users.')

def messageView(request):
    return HttpResponse({"This view is protected"})



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
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class MenuItemsView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer