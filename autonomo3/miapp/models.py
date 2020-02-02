from django.db import models

# Create your models here.



class Pizzerias(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    id_pizzeria = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    categories =models.CharField(max_length=200, null=True, blank=True)
    city=models.CharField(max_length=200, null=True, blank=True)
    country=models.CharField(max_length=200, null=True, blank=True)
    keys=models.CharField(max_length=200, null=True, blank=True)
    latitude=models.CharField(max_length=200, null=True, blank=True)
    longitude=models.CharField(max_length=200, null=True, blank=True)
    menuPageURL=models.CharField(max_length=200, null=True, blank=True)
    menusamountMax=models.CharField(max_length=200, null=True, blank=True)
    menusamountMin=models.CharField(max_length=200, null=True, blank=True)
    menuscurrency=models.CharField(max_length=200, null=True, blank=True)
    menusdateSeen=models.CharField(max_length=200, null=True, blank=True)
    menusdescription=models.CharField(max_length=200, null=True, blank=True)
    menusname=models.CharField(max_length=200, null=True, blank=True)
    name=models.CharField(max_length=200, null=True, blank=True)
    postalCode=models.CharField(max_length=200, null=True, blank=True)
    priceRangeCurrency=models.CharField(max_length=200, null=True, blank=True)
    priceRangeMin=models.CharField(max_length=200, null=True, blank=True)
    priceRangeMax=models.CharField(max_length=200, null=True, blank=True)
    province=models.CharField(max_length=200, null=True, blank=True)

