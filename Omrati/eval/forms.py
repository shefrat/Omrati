from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ("agencyName","dateOfTravel", "days", "price", "contract", "insurance", "theDate", "hotelRate", "commitmentDistance", "president", "presidentRate", "hotelName", "streetbus", "servicesOutside", "distanceHotel", "furniture", "conditioning", "bathroom", "towel", "roomClean", "wifi", "elevator", "food", "hotelNameMadina", "streetbusMadina", "servicesOutsideMadina", "distanceHotelMadina", "furnitureMadina", "conditioningMadina", "bathroomMadina", "towelMadina", "roomCleanMadina", "wifiMadina", "elevatorMadina", "foodMadina")