from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import Car
from .serializers import CarSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class CarsList(generics.ListCreateAPIView):
    permission_calss = (IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_calss = (IsAuthorOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer