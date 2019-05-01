from django.contrib import admin
from .models import Hotel, Agency, EvaluationAgency, EvaluationHotel, Rate

class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "city")

class AgencyAdmin(admin.ModelAdmin):
    list_display = ("name",)

class EvaluationHotelAdmin(admin.ModelAdmin):
    list_display = ("streetbus", "servicesOutside", "distanceHotel", "furniture", "conditioning", "bathroom", "towel", "roomClean", "wifi", "elevator", "food")

class EvaluationAgencyAdmin(admin.ModelAdmin):
    list_display = ("dateOfTravel", "days", "price", "contract", "insurance", "theDate", "hotelRate", "commitmentDistance", "president", "presidentRate")

class RateAdmin(admin.ModelAdmin):
    list_display = ("agencyid", "hotelMadina", "hotelMecca")


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(EvaluationHotel, EvaluationHotelAdmin)
admin.site.register(EvaluationAgency, EvaluationAgencyAdmin)
admin.site.register(Rate, RateAdmin)