from django.contrib import admin
from .models import Hotel, Agency, Evaluation

class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "city")

class AgencyAdmin(admin.ModelAdmin):
    list_display = ("name",)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("agencyName","dateOfTravel", "days", "price", "contract", "insurance", "theDate", "hotelRate", "commitmentDistance", "president", "presidentRate", "hotelName", "streetbus", "servicesOutside", "distanceHotel", "furniture", "conditioning", "bathroom", "towel", "roomClean", "wifi", "elevator", "food", "hotelNameMadina", "streetbusMadina", "servicesOutsideMadina", "distanceHotelMadina", "furnitureMadina", "conditioningMadina", "bathroomMadina", "towelMadina", "roomCleanMadina", "wifiMadina", "elevatorMadina", "foodMadina")


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Evaluation, EvaluationAdmin)