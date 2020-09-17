from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from pprint import pprint
import requests
import os
import json
from .Main import main
from .models import Challan
from datetime import datetime





def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "uploadpic.html")

    else:
        return render(request, "index.html")


def uploadimage(request):
    img = request.GET["image"]
    loc = request.GET["loc"]
    n = main("C:/Users/HP/PycharmProjects/numberplatedetection/numberplatedetection/LicPlateImages/"+img)
    si = Challan.objects.get(numberplate=n)
    date = datetime.now()

    return render(request, "ownerdetails.html", {'challan': si, 'loca': loc, 'dates': date})



def user(request):
    return render(request, "user.html")


def userval(request):
    a = request.GET["licence"]
    b = Challan.objects.get(numberplate=a)
    date = datetime.now()
    return render(request, "challandetail.html", {'challan': b})










