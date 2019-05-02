from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("stats", views.stats , name="stat"),
    path("eval", views.NewEvaluation , name="eval"),
]