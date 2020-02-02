from django.shortcuts import render
from rest_framework import generics, status

from .models import *
from .serializer import PizzaSerializer

# Create your views here.
class PizzeriasViewSet(generics.ListCreateAPIView):
    '''
    Contiene información sobre pizzerias
    '''
    queryset = Pizzerias.objects.all()
    #lookup_field = 'id'
    serializer_class = PizzaSerializer

class PizzeriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizzerias.objects.all()
    serializer_class = PizzaSerializer

