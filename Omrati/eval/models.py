from django.db import models
from django.db.models import Avg

class Hotel(models.Model):
    cities = (("Mecca", "مكّة"), ("Madina", "المدينة"))
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=10, choices=cities)

    def __str__(self):
        return str(self.name)

class Agency(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class EvaluationHotel(models.Model):
    streetbus = models.IntegerField(max_length=10, choices=((1, "نعم"), (0, "لا")))
    servicesOutside = models.IntegerField(max_length=10, choices=((1, "مطاعم"), (1, "مواد غذائيّة"),(1, "تسوّق")))
    distanceHotel = models.IntegerField(max_length=10, choices=((6, "قريبة"), (2, "متوسطة"),(0, "بعيدة")))
    furniture = models.IntegerField(max_length=10, choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")))
    conditioning = models.IntegerField(max_length=10, choices=((4, "نعم"), (0, "لا")))
    bathroom = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    towel = models.IntegerField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    roomClean = models.IntegerField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    wifi = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    elevator = models.IntegerField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    food = models.IntegerField(max_length=10, choices=((3, "نعم"), (0, "لا"), (2, "لا أعلم")))

    def __str__(self):
        return str(self.id)
    
class EvaluationAgency(models.Model):
    dateOfTravel = models.DateField()
    days = models.IntegerField()
    price = models.IntegerField()
    contract = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    insurance = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    theDate = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    hotelRate = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    commitmentDistance = models.IntegerField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    president = models.IntegerField(max_length=10, choices=((2, "كامل الرحلة"), (1, "جزء من الرحلة فقط"), (0, "لا")))
    presidentRate = models.IntegerField(max_length=10, choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")))

    def __str__(self):
        return str(self.id)

class Rate(models.Model):
    agencyid = models.ForeignKey(EvaluationAgency, on_delete=models.CASCADE, default=1)
    hotelMadina = models.ForeignKey(EvaluationHotel, on_delete=models.CASCADE, default=1, related_name="Madina")
    hotelMecca = models.ForeignKey(EvaluationHotel, on_delete=models.CASCADE, default=1, related_name="Mecca")
