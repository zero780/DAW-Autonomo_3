from rest_framework import serializers
from .models import *


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizzerias
        fields = ('id_pizzeria', 'address','categories','city','country','keys','latitude','longitude','menuPageURL','menusamountMax','menusamountMin',
                'menuscurrency','menusdateSeen','menusdescription','menusname','name','postalCode','priceRangeCurrency','priceRangeMin','priceRangeMax',
                  'province')
