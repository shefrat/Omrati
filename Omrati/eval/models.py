from django.db import models
from django.contrib.auth.models import AbstractUser

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

class Evaluation(models.Model):
    # Agency
    agencyName = models.ForeignKey(Agency, on_delete=models.CASCADE, default=1)
    dateOfTravel = models.DateField()
    days = models.IntegerField()
    price = models.IntegerField()
    contract = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    insurance = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    theDate = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    hotelRate = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    commitmentDistance = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    president = models.IntegerField(choices=((2, "كامل الرحلة"), (1, "جزء من الرحلة فقط"), (0, "لا")), default=1)
    presidentRate = models.IntegerField(choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")), default=1)
    # Total Points: 16

    # Mecca
    hotelName = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=1, related_name="Mecca")
    streetbus = models.IntegerField(choices=((1, "نعم"), (0, "لا")), default=1)
    servicesOutside = models.IntegerField(choices=((1, "مطاعم"), (1, "مواد غذائيّة"),(1, "تسوّق")), default=1)
    distanceHotel = models.IntegerField(choices=((6, "قريبة"), (2, "متوسطة"),(0, "بعيدة")), default=1)
    furniture = models.IntegerField(choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")), default=1)
    conditioning = models.IntegerField(choices=((4, "نعم"), (0, "لا")), default=1)
    bathroom = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    towel = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    roomClean = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    wifi = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    elevator = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    food = models.IntegerField(choices=((3, "نعم"), (0, "لا"), (2, "لا أعلم")), default=1)
    # Total Points: 38

    #Medina
    hotelNameMadina = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=1, related_name="Madina")
    streetbusMadina = models.IntegerField(choices=((1, "نعم"), (0, "لا")), default=1)
    servicesOutsideMadina = models.IntegerField(choices=((1, "مطاعم"), (1, "مواد غذائيّة"),(1, "تسوّق")), default=1)
    distanceHotelMadina = models.IntegerField(choices=((6, "قريبة"), (2, "متوسطة"),(0, "بعيدة")), default=1)
    furnitureMadina = models.IntegerField(choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")), default=1)
    conditioningMadina = models.IntegerField(choices=((4, "نعم"), (0, "لا")), default=1)
    bathroomMadina = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    towelMadina = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    roomCleanMadina = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    wifiMadina = models.IntegerField(choices=((2, "نعم"), (0, "لا")), default=1)
    elevatorMadina = models.IntegerField(choices=((5, "نعم"), (0, "لا")), default=1)
    foodMadina = models.IntegerField(choices=((3, "نعم"), (0, "لا"), (2, "لا أعلم")), default=1)
    # Total Points: 38

    # Others
    # st = (("Pending", "Pending"), ("Refused", "Refused"), ("Accepted", "Accepted"))
    # status = models.CharField(max_length=50, choices=st,default=st[0][0])
    # Total = 92

    def __str__(self):
        return str(self.id)

