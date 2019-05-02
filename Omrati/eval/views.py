from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Evaluation
from .forms import EvaluationForm
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def index(request):
    return HttpResponse("Hello, world!")

def stats(request):
    template = loader.get_template("eval/stats.html")
    # madinahotels = Evaluation.objects.filter(agencyName__name="وكالة ممتازة").count()
    x = 0
    for m in Evaluation.objects.filter(agencyName__name="وكالة ممتازة").all() :
        s = m.contract + m.insurance + m.theDate + m.hotelRate + m.commitmentDistance + m.president + m.presidentRate
        s += m.streetbus + m.servicesOutside + m.distanceHotel + m.furniture + m.conditioning + m.bathroom + m.towel + m.roomClean + m.wifi + m.elevator + m.food
        s += m.streetbusMadina + m.servicesOutsideMadina + m.distanceHotelMadina + m.furnitureMadina + m.conditioningMadina + m.bathroomMadina + m.towelMadina + m.roomCleanMadina + m.wifiMadina + m.elevatorMadina + m.foodMadina
        print(s)
    madinahotels = 1
    context = {"mh":madinahotels}
    return HttpResponse(template.render(context, request))

def NewEvaluation(request):
    template = loader.get_template("eval/evaluationform.html")
    form = EvaluationForm()
    context = {"f": form}
    if request.method == "POST":
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            # e = form.save()
            # request.user.Evaluation.add(e)
            return redirect(reverse('home'))
    return HttpResponse(template.render(context, request))
