from rest_framework.decorators import api_view
from .models import Menu
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .serializers import MenuSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pass

class SingleMenuView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pass

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer