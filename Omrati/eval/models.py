from django.db import models

class Hotel(models.Model):
    cities = (("Mecca", "مكّة"), ("Madina", "المدينة"))
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=10, choices=cities)


class Agency(models.Model):
    name = models.CharField(max_length=200)

class Evaluation(models.Model):
    streetbus = models.CharField(max_length=10, choices=((1, "نعم"), (0, "لا")))
    servicesOutside = models.CharField(max_length=10, choices=((1, "مطاعم"), (1, "مواد غذائيّة"),(1, "تسوّق")))
    distancehotel = models.CharField(max_length=10, choices=((6, "قريبة"), (2, "متوسطة"),(0, "بعيدة")))
    furniture = models.CharField(max_length=10, choices=((4, "جيد"), (2, "متوسطة"),(0, "سيء")))
    conditioning = models.CharField(max_length=10, choices=((4, "نعم"), (0, "لا")))
    bathroom = models.CharField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    towel = models.CharField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    roomclean = models.CharField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    wifi = models.CharField(max_length=10, choices=((2, "نعم"), (0, "لا")))
    elevator = models.CharField(max_length=10, choices=((5, "نعم"), (0, "لا")))
    food = models.CharField(max_length=10, choices=((3, "نعم"), (0, "لا"), (2, "لا أعلم")))
    